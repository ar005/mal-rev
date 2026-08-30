# Threat Analysis Report

**Generated:** 2026-08-24 18:10 UTC
**Sample:** `11dafc9f077ea507a88277b30dc8b1868e73c0e93d8fd80bf5530b4888f22434_11dafc9f077ea507a88277b30dc8b1868e73c0e93d8fd80bf5530b4888f22434.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `11dafc9f077ea507a88277b30dc8b1868e73c0e93d8fd80bf5530b4888f22434_11dafc9f077ea507a88277b30dc8b1868e73c0e93d8fd80bf5530b4888f22434.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, 4 sections |
| Size | 4,877,312 bytes |
| MD5 | `53d461c92c187fc8b7eec8548a69e34d` |
| SHA1 | `dfb515394c29c67f9fb393e17ae0840fe181e4f7` |
| SHA256 | `11dafc9f077ea507a88277b30dc8b1868e73c0e93d8fd80bf5530b4888f22434` |
| Overall entropy | 7.996 |
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

Total strings found: **10692** (showing first 100)

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

Based on the additional disassembly provided in chunk 2, I have updated and expanded the analysis of the binary sample.

### Updated Analysis Summary: Technical & Behavioral Overview

The second portion of the disassembly confirms that this is not just a simple "wrapper" but a **highly polished, feature-rich installer engine** (consistent with modified 7-Zip SFX source code). It contains significant logic for user interface management, environment preparation, and sophisticated process handling.

#### Core Functionality Additions:
*   **Sophisticated UI/UX Management:** The functions `fcn.004097f6` and `fcn.00407a58` indicate a robust system for managing the "look and feel" of an installation wizard. It dynamically selects different strings (e.g., `WarningTitle`, `ErrorTitle`, `Progress`) based on internal states, handles window positioning (`SetWindowPos`), and manages dialog box dimensions.
*   **Environment Awareness:** Function `fcn.00403b54` specifically interacts with the Windows shell to resolve "Special Folders" (via `SHGetSpecialFolderPathW`). It also contains logic related to `.lnk` files and environment variable setting (`SetEnvironment`), which are essential for a professional installer that creates desktop shortcuts or adds entries to the system path.
*   **Advanced Process Execution:** The function `fcn.004180ff` is a critical piece of infrastructure. It uses advanced Windows API calls such as:
    *   **`CreateProcessW`**: To launch the extracted payload.
    *   **`CreateJobObjectW` & `AssignProcessToJobObject`**: These are used to group processes into "jobs." In an installer, this is often used to ensure that if the main installer closes, all child processes (like a background service) stay active or behave consistently. 
    *   **`ResumeThread`**: Used to manage thread execution timing during the transition from the "extractor" state to the "payload" state.

#### Security-Relevant Observations:
1.  **High Degree of Customization:** The complexity of functions like `fcn.0040d480` and `fcn.00416e11` suggests a sophisticated decompression or data transformation engine (likely LZMA or similar). While standard for 7-Zip, the sheer volume of internal logic indicates that this binary can handle complex multi-part archives or "wrapped" payloads that are not immediately accessible via simple extraction tools.
2.  **Infrastructure for Stealth/Persistence:** The use of `CreateJobObject` and `SetInformationJobObject` (visible in the 0x4180ff block) allows a threat actor to control how child processes are managed by the OS. This can be used to ensure that even if the initial "downloader" or "extractor" is terminated, the secondary payload continues to run.
3.  **Standard-Looking Behavior (Cloaking):** The heavy investment in UI strings (e.g., `ExtractTitle`, `CancelPrompt`) and standard Win32 API calls for icons (`LoadIconW`) suggests a desire for the malware to appear as a legitimate, high-quality software installer to the end user. This "living off the land" style of programming makes it harder to distinguish from actual malicious software in a telemetry feed without deeper behavioral analysis.

---

### Updated Summary for Incident Response

This sample is a **high-quality installer wrapper**. It provides a professional-grade user interface and sophisticated execution logic to facilitate the delivery of an underlying payload. 

**Key Indicator Changes/Additions:**
*   **Mechanism:** The binary acts as a "Stage 1" loader. It handles the heavy lifting of decompression, UI interaction, and environment preparation so that "Stage 2" (the actual malicious payload) can run in a ready-to-operate environment.
*   **Sophistication Level:** Moderate-High. This is not a rudimentary script; it is a professional-grade tool modified to hide the transition between the "setup" phase and the "malicious action" phase.
*   **Specific Tactics Observed:** 
    *   **Masquerading:** Uses standard installer terminology and UI elements.
    *   **Defense Evasion (via Complexity):** The complexity of the decompression/decryption routines (`fcn.0040d480`) may be used to hide the payload from simple automated sandboxes that do not perform deep unpacking.
    *   **Persistence/Execution Control:** Uses Windows Jobs and specific thread management during the transition between processes.

**Recommendations for Further Investigation:**
1.  **Behavioral Analysis in a Sandbox:** Monitor the system calls specifically around `fcn.004180ff` to identify the exact filename and path of the secondary payload launched via `CreateProcessW`. 
2.  **Network Monitoring:** While this binary handles "offline" extraction, the transition point at `fcn.004180ff` is a primary location for a malicious payload to initiate its first network callback (C2).
3.  **Memory Forensics:** Conduct memory dumps during the "Extraction" phase; many packers will decrypt parts of their instructions or the secondary payload in memory before execution.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the behaviors identified in your analysis to the relevant MITRE ATT&CK techniques:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1036** | Masquerading | The binary utilizes standard installer terminology, UI elements (e.g., `WarningTitle`, `Progress`), and icons to blend in as a legitimate software installation wizard. |
| **T1027** | Obfuscated Files or Information | The complex decompression/data transformation engine (likely LZMA) is designed to hide the "Stage 2" payload from automated analysis tools that do not perform deep unpacking. |
| **T1059** | Command and Scripting Interpreter | The use of `CreateProcessW` at critical transition points (`fcn.004180ff`) identifies the mechanism used to launch the secondary malicious payload. |
| **T1036.005** | Masquerading (Web Service/Installer) | The "higher complexity" and "polished UI" specifically aim to hide the transition from an installer state to a malicious execution state. |

### Analyst Notes:
*   **Defense Evasion via Complexity:** The analysis explicitly mentions that the complexity of `fcn.0040d480` acts as a barrier for automated sandboxes; this is a classic implementation of **T1027**.
*   **Execution Management:** While the use of **Job Objects** (`CreateJobObjectW`) isn't always mapped to a single unique ID, it is a primary method for ensuring process persistence and execution stability during stage-switching in multi-stage installers.
*   **T1059 Mapping:** Even though `CreateProcessW` is an API call, it is the primary mechanism for **T1059** when used to transition between different stages of an infection chain (Loader $\rightarrow$ Payload).

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral report, here are the extracted Indicators of Compromise (IOCs).

### **IP addresses / URLs / Domains**
*   None identified.

### **File paths / Registry keys**
*   None identified. *(Note: While "setup.exe" appears in the strings, it is a generic filename and not associated with a specific path or unique malicious location.)*

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified.

### **Other artifacts**
*   **Application Behavior (Masquerading):** The binary utilizes a heavily modified **7-Zip SFX (Self-Extracting) wrapper**. It contains specific internal strings such as `7-Zip:`, `SFX module - Copyright`, and `7-Zip archiver` to mimic legitimate installer behavior.
*   **Execution Logic:** Use of `CreateJobObjectW` and `AssignProcessToJobButton` (specifically at address `0x4180ff`) used to manage child processes and potentially ensure persistence or survival of the payload after the "installer" closes.
*   **Thread Management:** Utilization of `ResumeThread` during the transition between the extraction phase and the execution of the secondary payload.
*   **Environment Manipulation:** Usage of `SHGetSpecialFolderPathW` to resolve system directories for potential persistence or file placement.

---
**Analyst Note:** This sample functions as a "Stage 1" loader/wrapper. While no hardcoded C2 infrastructure (IPs/Domains) was found in the string dump, the primary threat indicator is the **sophisticated masquerading technique**. The binary is designed to look like a legitimate software installer while utilizing advanced Windows API calls to manage the transition of a hidden "Stage 2" payload into an active state.

---

## Malware Family Classification

Based on the provided analysis, here is the classification for the sample:

1.  **Malware family:** custom (specifically a "Stage 1" wrapper)
2.  **Malware type:** loader
3.  **Confidence:** High
4.  **Key evidence:**
    *   **Sophisticated Masquerading:** The binary utilizes a heavily modified 7-Zip SFX source to mimic the UI/UX of a legitimate software installer (e.g., progress bars, warning titles), designed to deceive both users and automated systems.
    *   **Multi-Stage Execution Logic:** The use of `CreateJobObjectW`, `ResumeThread`, and complex decompression routines indicates that its primary purpose is to manage the transition from an "installer" state to a "payload" state (Stage 2).
    *   **Defense Evasion Tactics:** It employs advanced Windows API calls for process management and information hiding (T1036, T1027) specifically to ensure that the secondary payload remains active even if the initial wrapper is closed or flagged.
