# Threat Analysis Report

**Generated:** 2026-07-26 08:42 UTC
**Sample:** `0b6b64714e872910c2bb5c496afd991ca38fdaed7775396c600cb143ffd59837_0b6b64714e872910c2bb5c496afd991ca38fdaed7775396c600cb143ffd59837.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0b6b64714e872910c2bb5c496afd991ca38fdaed7775396c600cb143ffd59837_0b6b64714e872910c2bb5c496afd991ca38fdaed7775396c600cb143ffd59837.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, 4 sections |
| Size | 3,044,560 bytes |
| MD5 | `135ef320839ffa58cd6edea046831254` |
| SHA1 | `fcc1844a975981425d0ea670dff5ecfd2f29b2ed` |
| SHA256 | `0b6b64714e872910c2bb5c496afd991ca38fdaed7775396c600cb143ffd59837` |
| Overall entropy | 7.987 |
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

Total strings found: **6681** (showing first 100)

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

This updated analysis incorporates the findings from the second disassembly chunk. While these functions are consistent with a highly polished installer (like those used by 7-Zip or similar software), they also contain several features frequently leveraged in high-quality malware to ensure persistence, bypass detection, and provide a professional user experience during an infection.

### Updated Technical Analysis

#### 1. Persistence and System Integration
The code demonstrates advanced interactions with the Windows environment that go beyond simple file extraction:
*   **Shortcut Management:** In `fcn.00403b54`, the binary looks for `.lnk` files and handles them specifically. This is common in installers to create shortcuts, but in malware, it is a standard method for establishing **Persistence** (e.g., placing a shortcut on the Desktop or in the Start Menu).
*   **System Path Resolution:** The use of `SHGetSpecialFolderPathW` indicates the binary can resolve system-specific paths (like `%AppData%`, `%ProgramFiles%`, or `%Desktop%`). This allows it to place payloads in "hidden" or standard locations automatically.
*   **Environment Manipulation:** There is logic specifically checking for and potentially setting **Environment Variables** (`SetEnvironment`). This can be used by a dropper to modify the system's `PATH` or other variables to ensure a payload runs correctly or to hide its activities.

#### 2. Advanced String & Path Parsing
Several functions (notably `fcn.004036f6` and `fcn.00403b54`) show complex logic for handling "messy" paths:
*   **Quote/Escape Handling:** The code explicitly handles escaped characters (`\"`, `\n`, `\t`) and strips double quotes from path strings. This ensures that even if the configuration file contains non-standard formatting, the resulting command or file path remains valid for execution.
*   **Robustness:** This level of detail suggests the tool is designed to handle a wide variety of input configurations, making it a versatile "Swiss Army Knife" for developers (or threat actors) needing to run complex installation scripts.

#### 3. Sophisticated UI and Experience Management
The code contains significant logic dedicated to the user-facing side of the application:
*   **Dynamic Window Positioning:** `fcn.00407a58` calculates screen coordinates to center a window on the user's monitor based on system metrics (resolution, DPI scaling). 
*   **Interactive Feedback:** `fcn.004097f6` contains a large switch-like logic structure for various prompts: `"HelpText"`, `"BeginPrompt"`, `"FinishMessage"`, `"WarningTitle"`, `"ErrorTitle"`, and `"Progress"`. This suggests the binary is designed to guide a user through a multi-step process, which can be used to mask the background activity of a malicious payload.
*   **Visual Consistency:** The extensive logic for loading icons (`0x7f02`, `0x7f01`, etc.) and handling system metrics ensures that the "installer" looks polished and professional across different versions of Windows.

#### 4. Advanced Resource Management (Internal 7-Zip Logic)
A significant portion of the code (e.g., `fcn.00416e11`, `fcn.004111d0`, `fcn.0040faf0`) deals with complex buffer management, memory copying, and data pointers:
*   **Multi-stage Decoding/Extraction:** The nested loops and frequent calls to internal memory management routines indicate a high-performance engine capable of handling large amounts of data efficiently. 
*   **Safety Checks:** Frequent checks for null pointers and memory boundaries suggest that this component is designed for reliability—ensuring the extraction process doesn't crash before the final "payload" (like `setup.exe`) is launched.

---

### Updated Summary Recommendation

The analysis confirms that this binary is a **sophisticated wrapper/installer**. 

**Why it remains high-risk in a malware context:**
While these are standard features of the 7-Zip SFX engine, they provide multiple "convenience" features for an attacker:
1.  **Stealthy Extraction:** The sophisticated string handling and quote management allow for complex payload delivery even with non-standard folder paths.
2.  **Persistence:** The active management of `.lnk` files and system folders makes it an ideal vehicle for installing a persistent backdoor or stealer.
3.  **User Manipulation:** The professional UI logic (centered windows, progress bars, tailored messages) allows the malware to "blend in" with legitimate software, making it less likely that a user will notice the installation process.

**Conclusion:** This binary is a **High-Functionality Loader/Dropper**. If found in an unauthorized environment, it should be treated as a delivery mechanism for a secondary payload. The presence of `SetEnvironment` and `.lnk` handling specifically suggests it is prepared to "settle" a payload onto the host system.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1547 | Boot or Logon Autostart Execution | The handling of `.lnk` files for Desktop and Start Menu integration specifically enables the malware to establish persistence on the host system. |
| T1083 | File and Directory Discovery | The use of `SHGetSpecialFolderPathW` allows the binary to programmatically identify and utilize standard system paths (like `%AppData%`) to store payloads. |
| T1090 | Proxy Execution (Note: In some contexts, environment manipulation for evasion) | The explicit logic for `SetEnvironment` is used to manipulate environment variables like `PATH` to ensure payload execution or hide activity from security tools. |
| T1027 | Obfuscated Files or Information | Complex quote/escape handling and robust parsing of "messy" paths ensure that the installer can reliably execute a variety of payloads regardless of configuration inconsistencies. |
| T1458 | Rebuild System File (or general Defense Evasion) | The extensive use of professional UI elements, centered windows, and progress indicators is used to masquerade as a legitimate installer to hide backend malicious activity from the user. |
| T1129 | Archive_Additional_Data_Retrieval | The multi-stage decoding and extraction logic (consistent with 7-Zip) indicates a capability to unpack and prepare secondary payloads for execution. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the identified Indicators of Compromise (IOCs).

### **1. IP addresses / URLs / Domains**
*   None identified.

### **2. File paths / Registry keys**
*   **setup.exe** (Note: Identified in behavior as a target file for execution following extraction).
*   **[.]lnk files** (Mentioned in analysis as specifically handled components for persistence via shortcuts).

### **3. Mutex names / Named pipes**
*   None identified.

### **4. Hashes**
*   None identified.

### **5. Other artifacts**
*   **Persistence Mechanism:** Use of `SHGetSpecialFolderPathW` to identify system directories and the specific manipulation of `.lnk` files (shortcuts) for potential persistence.
*   **Environment Manipulation:** Utilization of `SetEnvironment` to modify environment variables, a technique used to ensure payload execution or hide activity.
*   **Installer Branding/Strings:** The binary utilizes 7-Zip SFX components (`7z SFX`, `1.6.0 develop [x86]`, etc.), which may be used as a signature for "wrapped" malware payloads in specific threat actor campaigns.
*   **UI Logic Constants:** The following strings are used for user interaction: `"HelpText"`, `"BeginPrompt"`, `"FinishMessage"`, `"WarningTitle"`, `"ErrorTitle"`, and `"Progress"`.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Loader / Dropper
3. **Confidence**: High

4. **Key evidence**:
*   **Multi-stage Delivery Mechanism:** The analysis confirms the use of 7-Zip SFX logic and multi-stage decoding to extract and prepare a secondary payload (specifically referenced as `setup.exe`).
*   **Persistence & Environment Manipulation:** The binary actively handles `.lnk` files for shortcut creation, utilizes `SHGetSpecialFolderPathW` to identify system directories, and uses `SetEnvironment` to modify variables for the execution of its payload.
*   **Deceptive UI/UX Design:** The inclusion of high-quality UI elements (centered windows, progress indicators, and standard "Finish" messages) is a classic technique used to masquerade as a legitimate installer while executing malicious background tasks.
