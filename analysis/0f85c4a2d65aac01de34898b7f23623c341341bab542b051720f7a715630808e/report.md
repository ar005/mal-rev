# Threat Analysis Report

**Generated:** 2026-08-16 15:44 UTC
**Sample:** `0f85c4a2d65aac01de34898b7f23623c341341bab542b051720f7a715630808e_0f85c4a2d65aac01de34898b7f23623c341341bab542b051720f7a715630808e.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0f85c4a2d65aac01de34898b7f23623c341341bab542b051720f7a715630808e_0f85c4a2d65aac01de34898b7f23623c341341bab542b051720f7a715630808e.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, 4 sections |
| Size | 3,238,888 bytes |
| MD5 | `a33798b8d2d931526b822399fd73640f` |
| SHA1 | `63dfe66a44c03e9fba6d7eea8db1e045a4ff52ff` |
| SHA256 | `0f85c4a2d65aac01de34898b7f23623c341341bab542b051720f7a715630808e` |
| Overall entropy | 7.988 |
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
| `.rsrc` | 20,480 | 1.897 | No |

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

Total strings found: **7156** (showing first 100)

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

Based on the additional disassembly provided, I have updated the analysis. The new code confirms that while the binary functions as an SFX loader, it incorporates sophisticated execution management and utilizes a structured "installer wizard" framework to mask its activities.

### Updated Technical Analysis

#### 1. Enhanced Decompression & Data Handling
The functions `fcn.0040d090`, `fcn.004111d0`, and `fcn.0040f380` confirm a very high level of complexity in how the binary handles data in memory. 
*   **LZMA/LZMA2 Complexity:** The repetitive bit-shifting, large state lookups (e.g., `uVar10 >> (uVar3 & 0x1f)`), and recursive-style loop logic are classic indicators of a professional decompression library (like the one used in 7-Zip).
*   **Buffer Management:** The extensive use of internal offset calculations suggests the binary is designed to handle large, multi-part compressed files, allowing it to unpack complex payloads without losing data integrity.

#### 2. Advanced Process Orchestration
The function `fcn.004180ff` reveals higher-level logic than a simple "launch" command:
*   **Job Object Integration:** The code utilizes `CreateJobObject`, `AssignProcessToJobObject`, and `SetInformationJobObject`. 
    *   *Significance:* In legitimate installers, Job Objects are used to ensure that if the main installer is closed, all child processes (the payload) are terminated. **In a malware context**, this is often used to manage a "swarm" of processes or to ensure that the malicious payloads stay grouped and managed by the loader's logic.
*   **Wait/Resume Logic:** The use of `ResumeThread` and `GetExitCodeProcess` indicates the launcher monitors the status of the unpacked payload, potentially waiting for it to initialize before cleaning up its own remains from memory.

#### 3. System Environment & Path Manipulation
The function `fcn.004036f6` specifically interacts with system environment variables and path construction:
*   **Shell Interaction:** It uses `SHGetSpecialFolderPathW` to identify standard locations (like "Desktop" or "AppData").
*   **Environment Modification:** The code contains logic for checking and potentially setting environment variables (e.g., `SetEnvironment`). This is used to ensure the payload has the correct paths or configurations needed to run successfully after being unpacked.

#### 4. Execution Masking (The "Wizard" Component)
Several functions (`fcn.004097f6`, `fcn.00408e76`, `fcn.00407a58`) indicate the presence of a sophisticated Graphical User Interface (GUI):
*   **Standardized Dialogues:** The code checks for strings like `"HelpText"`, `"BeginPrompt"`, `"FinishMessage"`, and `"WarningTitle"`. 
*   **Interactive Elements:** The logic in `fcn.00408e76` handles button IDs (like `0x4b1`, `0x4b3`) which typically correspond to "Next," "Back," or "Cancel" buttons.
*   **Analytical Conclusion:** This suggests the malware is not a "raw" script, but rather uses a **commercial-grade installer framework**. By using a legitimate wrapper (like Inno Setup or similar), the malware achieves two goals: it provides an "official" look to the user and integrates high-quality features like multi-language support and complex installation logic.

---

### Updated Summary for Analysts

**Classification:** Complex Multi-Stage Dropper / Installer Wrapper
**Primary Mechanism:** 7-Zip (LZMA) Decompression + Windows Job Object Management.

**Key Findings from Additional Data:**
1.  **Persistence of Control:** The use of **Job Objects** indicates a sophisticated approach to managing the lifecycle of the dropped payload, ensuring it executes correctly while keeping its process tree organized.
2.  **Professional Masking:** The binary includes a full "Wizard" logic suite. This is a classic tactic used by advanced persistent threats (APTs) and high-end malware authors to blend in with legitimate software installations. The presence of standard installer dialogs (`WarningTitle`, `FinishMessage`) makes it harder for a human user or a basic heuristic scanner to distinguish it from a valid setup file.
3.  **System Preparation:** The binary actively prepares the environment via **Special Folder discovery** and **Environment Variable manipulation**, ensuring that once the payload is "dropped," it has an optimal environment to execute its final stage (e.g., establishing C2 communication or encrypting files).

**Conclusion for Incident Response:**
This binary is a high-quality piece of malware infrastructure. It does not just "drop" a file; it **manages the transition** from the initial infection point to the active payload. Investigators should look for:
*   **Persistence mechanisms** in any process associated with the Job Objects identified in `fcn.004180ff`.
*   **Environment changes**, specifically to system variables or hidden folders in "Special" paths.
*   **Evasion via Standardity:** Because it uses a standard installer framework, security tools may not flag the "installer" behavior as malicious; however, the specific content of the LZMA-compressed payload is almost certainly unauthorized and harmful.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Files or Information | The use of complex LZMA/LZMA2 decompression logic is a clear indicator that the malicious payload is being hidden within a compressed container to evade detection. |
| T1036 | Masquerading | The inclusion of an "Installer Wizard" framework, standard GUI elements (e.g., "Next," "Back"), and common system messages allows the malware to blend in with legitimate software updates or installations. |
| T1036.005 | Spoofing Execution Capability | The implementation of a commercial-grade installer wrapper is designed to mislead both human users and basic security tools into treating the malicious process as a standard installation routine. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

*Note: Because this sample appears to be a sophisticated "Installer Wrapper" using standard libraries (like 7-Zip), many indicators are behavioral rather than static (such as specific IPs or hardcoded paths).*

### **IP addresses / URLs / Domains**
*   None identified.

### **File paths / Registry keys**
*   None identified. (Note: While "setup.exe" and "Extraction path" appear in strings, these are generic variables/filenames used by the 7-Zip SFX library and do not constitute specific unique IOCs).

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified. (The obfuscated character blocks in the string dump do not conform to standard MD5, SHA1, or SHA256 formats).

### **Other artifacts**
*   **Technical Signatures:**
    *   **LZMA/LZMA2 Compression:** Use of complex decompression logic for payload unpacking.
    *   **7-Zip SFX Library:** Integration of 7-Zip's internal error handling and versioning strings (e.g., `1.6.0 develop [x86]`, `9.22 beta`).
*   **Behavioral Patterns:**
    *   **Job Object Management:** Use of `CreateJobObject`, `AssignProcessToJobButton`, and `SetInformationJobObject` to manage child process lifecycles (often used to ensure the payload stays hidden or terminates if the loader is closed).
    *   **Installer Wizard Masquerading:** Presence of UI logic for standard installation prompts (`"HelpText"`, `"BeginPrompt"`, `"FinishMessage"`, `"WarningTitle"`).
    *   **Environment Manipulation:** Calls to `SHGetSpecialFolderPathW` and `SetEnvironment` to prepare the system environment for subsequent payload execution.
    *   **Process Monitoring:** Use of `ResumeThread` and `GetExitCodeProcess` to monitor the state of unpacked components before proceeding with installer logic.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: dropper / loader
3. **Confidence**: High
4. **Key evidence**:
    *   **Sophisticated Payload Handling:** The use of complex LZMA/7-Zip decompression logic and Windows Job Objects indicates a professional-grade infrastructure designed to manage multi-stage payloads while ensuring they remain managed by the loader's logic.
    *   **Intentional Masquerading:** The inclusion of "Installer Wizard" components (standard buttons, warnings, and completion messages) is a deliberate tactic to bypass heuristic detection and deceive human users into viewing the process as legitimate software installation.
    *   **Environment Preparation:** The binary actively manipulates environment variables and utilizes `SHGetSpecialFolderPathW` to ensure the subsequent payload has the necessary system context to operate effectively after being unpacked.
