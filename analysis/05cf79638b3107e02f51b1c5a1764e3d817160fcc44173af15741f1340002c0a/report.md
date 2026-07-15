# Threat Analysis Report

**Generated:** 2026-07-14 17:49 UTC
**Sample:** `05cf79638b3107e02f51b1c5a1764e3d817160fcc44173af15741f1340002c0a_05cf79638b3107e02f51b1c5a1764e3d817160fcc44173af15741f1340002c0a.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `05cf79638b3107e02f51b1c5a1764e3d817160fcc44173af15741f1340002c0a_05cf79638b3107e02f51b1c5a1764e3d817160fcc44173af15741f1340002c0a.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, 4 sections |
| Size | 3,152,312 bytes |
| MD5 | `850b51dcabd5bbd6e62d31b004d3dfcd` |
| SHA1 | `ceea4ac9be1b502e4ab237f2b032b2551b351d53` |
| SHA256 | `05cf79638b3107e02f51b1c5a1764e3d817160fcc44173af15741f1340002c0a` |
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

Total strings found: **7249** (showing first 100)

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

Based on the second batch of disassembly, I have updated and expanded the analysis of the binary sample. The additional code reinforces the initial assessment that this is a **complex wrapper/dropper** while providing more specific technical details regarding how it interacts with the operating system to prepare for payload execution.

---

### Updated Analysis Report

#### 1. Core Functionality & Persistence (Enhanced)
The analysis confirms a sophisticated internal engine, likely derived from or heavily mimicking the **7-Zip SFX infrastructure**. The following features are now clearly visible:
*   **Comprehensive UI/UX Handling:** Functions such as `fcn.004097f6` and `fcn.00407a58` show extensive logic for managing "WarningTitle," "ErrorTitle," "Progress" bars, and "ExtractTitle." This indicates a polished installer interface designed to appear legitimate to the end-user.
*   **Environment Interaction:** The code includes routines (e.g., `fcn.004036f6`) that specifically look for "SetEnvironment" logic. This is used by installers to configure paths and system variables so that subsequent programs can run correctly. In a malware context, this is often used to manipulate the path of legitimate tools or set up environment variables that facilitate subsequent stages of an infection.
*   **System Integration:** The inclusion of `SHGetSpecialFolderPathW` (in `fcn.00403b54`) indicates the program can identify and utilize standard Windows directories (like Desktop, Documents, or AppData) to store its payload after extraction.

#### 2. Dropper & Payload Execution Logic (New Findings)
The second set of code contains several "smoking guns" for functionality typical of a sophisticated dropper:
*   **Process Spawning (`CreateProcessW`):** The function **`fcn.00405489`** is highly significant. It retrieves the command line, constructs a new execution string (including potential flags or paths), and calls `CreateProcessW`. This is the point where the "installer" finishes its job and launches the actual payload.
*   **Job Object Usage:** Inside the same function (`fcn.00405489`), the code utilizes **`CreateJobObject`**, **`AssignProcessToJobObject`**, and **`SetInformationJobObject`**. While these are legitimate tools for managing process groups in installers, they are also used by malware to ensure that child processes (the payloads) persist or are handled consistently if the primary installer is closed.
*   **Automatic Cleanup/Transition:** The logic suggests a "handoff" mechanism. Once `CreateProcessW` is called and the environment is prepared via the previously identified `SetEnvironment` checks, the installer is designed to relinquish control or close itself, leaving the payload running in memory or as a separate process.

#### 3. Technical Complexity & Obfuscation
*   **Data Processing Loops:** Functions like `fcn.004111d0` and `fcn.00410050` contain heavy iterations and complex logic to handle data buffers. This suggests the code is not just a simple script; it is designed to process compressed data or manipulated strings, making it harder for automated scanners to "see" the final payload until it is actually unpacked in memory.
*   **Obfuscated Constants:** The function **`fcn.0040ac20`** contains hardcoded hex constants (e.g., `0x6a09e667`, `0xbb67ae85`). These are often characteristic of custom hashing, decryption routines, or state machines used to process internal data structures during the extraction phase.

#### 4. Updated Risk Profile
*   **Type:** Advanced SFX Dropper / Wrapper.
*   **Primary Purpose:** To provide a "veneer" of legitimacy (using standard installer UI and 7-zip logic) while successfully extracting, configuring the environment for, and launching a hidden payload.
*   **Malicious Indicators:**
    1.  **Stealthy Execution:** The use of `CreateProcessW` in combination with `SetEnvironment` and `JobObjects` indicates a deliberate effort to "set the stage" for an secondary process.
    2.  **Anti-Analysis/Complexity:** The complexity of the internal buffer management suggests that the payload is heavily hidden within a multi-layer archive or encrypted container.
    3.  **Deceptive Nature:** By using 7-zip's signature logic and "Help" text, it successfully mimics legitimate software to evade basic heuristic detections.

### Summary for Incident Response / Security Report
The binary functions as a **sophisticated stage-1 dropper**. It is designed to masquerade as a standard installer (potentially for something like a game or utility) while performing several high-risk actions: 
1.  **Environment Manipulation:** Preparing the OS for the payload via `SetEnvironment`.
2.  **Extraction & Staging:** Utilizing complex routines to unpack data into system-friendly folders.
3.  **Execution Handoff:** Using `CreateProcessW` with Job Objects to launch a secondary, likely malicious, executable.

**Recommendation:** This binary should be treated as a high-risk delivery vehicle. Any process it spawes should be immediately isolated and analyzed, as the "true" payload (the intended malware) is launched only after this installer completes its routine.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1036.005 | Masquerading: Capability | The binary mimics 7-Zip SFX infrastructure and includes polished UI elements (Progress bars, Error titles) to appear as a legitimate installer. |
| T1134 | Modify Environment Variables | The inclusion of `SetEnvironment` logic is used to configure system variables to facilitate the execution of subsequent malicious components. |
| T1570 | Archive Extraction | The binary utilizes complex internal loops and buffer management to unpack data from a container, mirroring 7-zip extraction behaviors. |
| T1027 | Obfuscated Files or Information | The use of hardcoded hex constants and complex processing logic suggests the payload is hidden within a multi-layer archive or encrypted container. |
| T1059 | Command and Scripting Interpreter | The usage of `CreateProcessW` to perform a "handoff" allows the installer to launch the actual payload as a separate process. |
| T1204 | User Execution | (Optional/Contextual) The "veneer of legitimacy" provided by the polished UI is designed to trick a user into executing the initial dropper. |

***

**Analyst Notes:**
*   **T1570 (Archive Extraction)** is specifically mapped due to the identification of 7-Zip SFX logic, which is a common method for delivery and staging.
*   **T1134 (Modify Environment Variables)** is flagged because it specifically prepares the system environment (e.g., Path variables) to ensure the malicious payload executes correctly once launched.
*   The use of **Job Objects** alongside `CreateProcessW` is a high-fidelity indicator for persistence; it ensures that the child process remains active even if the "installer" shell is closed by the user.

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs).

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   **setup.exe** (Identified as a core component/target for execution during the extraction phase).
*   Note: While `SHGetSpecialFolderPathW` and `SetEnvironment` are mentioned, they refer to system-level API calls rather than specific hardcoded malicious file paths.

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *No standard cryptographic hashes (MD5/SHA1/SHA256) were found in the provided text.*

### **Other artifacts**
*   **Hardcoded Constants:** 
    *   `0x6a09e667`
    *   `0xbb67ae85`
    *(Note: These are identified as constants used for internal data processing, potentially decryption or hashing of configuration files.)*
*   **Behavioral Patterns / Techniques:**
    *   **SFX Wrapper:** Use of a 7-Zip SFX (Self-Extracting) wrapper to mask the primary payload.
    *   **Process Manipulation:** Utilization of `CreateJobObject`, `AssignProcessToJobObject`, and `SetInformationJobObject` to manage child process persistence/lifecycles.
    *   **Environment Modification:** Use of `SetEnvironment` to manipulate system variables prior to payload execution.
    *   **Execution Handoff:** The use of `CreateProcessW` to transition from the "installer" environment to a secondary, potentially malicious, executable.
    *   **Known Library Strings:** References to 7-Zip versions (1.6.0, 9.22) used to blend in with legitimate installer behaviors.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: dropper
3. **Confidence**: High
4. **Key evidence**:
    *   **Masquerading via SFX Wrapper:** The binary intentionally mimics 7-Zip SFX infrastructure to appear as a legitimate installer, utilizing standard UI elements (progress bars, error titles) to deceive the user and bypass heuristic detection.
    *   **Sophisticated Handoff Mechanism:** The use of `CreateProcessW` in conjunction with `CreateJobObject` and `SetEnvironment` indicates a deliberate "stage-one" design intended to prepare the environment and ensure the persistence of the secondary payload after the wrapper exits.
    *   **Obfuscated Extraction Logic:** The presence of complex data processing loops and hardcoded hex constants suggests that the final malicious payload is hidden within an encrypted or multi-layered archive, which is only unpacked during execution.
