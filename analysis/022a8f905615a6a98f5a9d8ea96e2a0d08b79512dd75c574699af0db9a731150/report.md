# Threat Analysis Report

**Generated:** 2026-06-28 02:18 UTC
**Sample:** `022a8f905615a6a98f5a9d8ea96e2a0d08b79512dd75c574699af0db9a731150_022a8f905615a6a98f5a9d8ea96e2a0d08b79512dd75c574699af0db9a731150.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `022a8f905615a6a98f5a9d8ea96e2a0d08b79512dd75c574699af0db9a731150_022a8f905615a6a98f5a9d8ea96e2a0d08b79512dd75c574699af0db9a731150.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, 4 sections |
| Size | 94,208 bytes |
| MD5 | `e8408a211ade214e5a80cc310d63e347` |
| SHA1 | `853da8240ad3eb6f99743dd686dc98872fa06e86` |
| SHA256 | `022a8f905615a6a98f5a9d8ea96e2a0d08b79512dd75c574699af0db9a731150` |
| Overall entropy | 6.022 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1483645813 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 61,440 | 6.057 | No |
| `.rdata` | 20,480 | 5.368 | No |
| `.data` | 4,096 | 0.576 | No |
| `.rsrc` | 4,096 | 6.666 | No |

### Imports

**KERNEL32.dll**: `GetModuleFileNameA`, `GetLongPathNameA`, `CreateMutexA`, `OpenMutexA`, `Process32Next`, `Process32First`, `CreateToolhelp32Snapshot`, `SizeofResource`, `LockResource`, `LoadResource`, `FindResourceA`, `GetLocaleInfoA`, `Process32NextW`, `Process32FirstW`, `lstrlenA`
**USER32.dll**: `GetWindowTextLengthA`, `GetForegroundWindow`, `UnhookWindowsHookEx`, `CloseClipboard`, `GetClipboardData`, `OpenClipboard`, `SetClipboardData`, `EmptyClipboard`, `ExitWindowsEx`, `MessageBoxA`, `GetKeyboardLayoutNameA`, `GetWindowThreadProcessId`, `ShowWindow`, `CloseWindow`, `GetWindowTextA`
**GDI32.dll**: `CreateDCA`, `CreateCompatibleDC`, `GetDeviceCaps`, `CreateCompatibleBitmap`, `SelectObject`, `StretchBlt`, `GetObjectA`, `GetDIBits`, `DeleteObject`, `DeleteDC`
**ADVAPI32.dll**: `OpenProcessToken`, `LookupPrivilegeValueA`, `AdjustTokenPrivileges`, `RegCreateKeyExA`, `RegQueryInfoKeyA`, `RegEnumKeyExA`, `RegEnumValueA`, `RegDeleteValueA`, `RegCreateKeyA`, `RegSetValueExA`, `RegOpenKeyExA`, `RegDeleteKeyA`, `RegCloseKey`, `RegQueryValueExA`, `GetUserNameW`
**SHELL32.dll**: `ShellExecuteA`, `ExtractIconA`, `Shell_NotifyIconA`, `ShellExecuteExA`, `ShellExecuteW`
**MSVCP60.dll**: `?begin@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QAEPADXZ`, `?end@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QAEPADXZ`, `?assign@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QAEAAV12@ABV12@@Z`, `?replace@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QAEAAV12@IIPBD@Z`, `??8std@@YA_NPBDABV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@0@@Z`, `??Y?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QAEAAV01@PBD@Z`, `??4?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QAEAAV01@ABV01@@Z`, `??0?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QAE@ABV?$allocator@G@1@@Z`, `?find_last_of@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QBEIDI@Z`, `??9std@@YA_NABV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@0@PBG@Z`, `??Y?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QAEAAV01@G@Z`, `?substr@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QBE?AV12@II@Z`, `?rfind@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QBEIGI@Z`, `?npos@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@2IB`, `?find@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QBEIPBDII@Z`
**MSVCRT.dll**: `_wrename`, `_controlfp`, `__set_app_type`, `__p__fmode`, `__p__commode`, `_adjust_fdiv`, `__setusermatherr`, `_initterm`, `__getmainargs`, `_acmdln`, `_XcptFilter`, `_exit`, `_onexit`, `__dllonexit`, `??1type_info@@UAE@XZ`
**WINMM.dll**: `waveInOpen`, `waveInStop`, `waveInClose`, `waveInAddBuffer`, `waveInPrepareHeader`, `waveInUnprepareHeader`, `waveInStart`
**SHLWAPI.dll**: `PathFileExistsA`
**WS2_32.dll**: `htons`, `gethostbyname`, `closesocket`, `socket`, `send`, `WSAGetLastError`, `connect`, `recv`, `WSAStartup`
**urlmon.dll**: `URLDownloadToFileA`
**gdiplus.dll**: `GdipLoadImageFromStreamICM`, `GdipDisposeImage`, `GdipCloneImage`, `GdipAlloc`, `GdipSaveImageToStream`, `GdipSaveImageToFile`, `GdipLoadImageFromStream`, `GdiplusStartup`, `GdipGetImageEncoders`, `GdipFree`, `GdipGetImageEncodersSize`
**WININET.dll**: `InternetCloseHandle`, `InternetOpenUrlA`, `InternetOpenA`, `InternetReadFile`

## Extracted Strings

Total strings found: **641** (showing first 100)

```
!This program cannot be run in DOS mode.
$
vu^viq^
wu^&ps^
vu^vi~^
vu^Rich
`.rdata
@.data
;utV
YYPVhT
PPQh
"@
SSVh#(@
tl9~8tg
8F4t{8
F<;F8r
8^5uu8
;utV
WWVh,8@
9>uWWVh8@
WWVh;8@
8^9u=8^8W
uSSVh8@
SSVh;8@
SSVhJ8@
W8^9t@
8^8t'8^9
#twHt`HtIHt2Ht
Bt`HtIHt2Ht
vtdHtPHt<Ht(Ht
tTIt=It,It
t=It,It
t]ItIIt2It
t<It(It
2twHt`HtIHt2Ht
gtaHtMHt9Ht)Ht


uD8^-u
utCHt.
u@@FF
t3Jt(Jt Jt
HHt4Ht
HHt4Ht
u@@FF:
u@@FF:
PPPhr^@
VWVPh`
uGG@@
VPhXA
tV950YA
uVVVhW
VWj
hL
u$WVVVV
YtWWW
;F4u
P
u@@FF
u@@FF
@VWj3
t VVVj
j
XPVSS
SbieDll.dll
HARDWARE\ACPI\DSDT\VBOX__
PROCMON_WINDOW_CLASS
PROCEXPL
invalid vector<T> subscript
?playaudio
%Y-%m-%d %H.%M
getcamsingleframe
nocamera
startcamcap
closecam
getcamframe
initcamcap
FreeFrame
GetFrame
CloseCamera
OpenCamera
camdlldata
camframe
[DataStart]
[DataStart]0000
%02i:%02i:%02i:%03i [KeepAlive] 
Enabled! (Timeout: %i seconds)

Timeout changed to %i

Disabled.

Timeout expired, resetting connection.

eventvwr.exe
Software\Classes\mscfile\shell\open\command
origmsc
mscfile\shell\open\command
searchfinished
filefound
searchwrongpath
searchstarted
offlinelogs
autofflinelogs

{ User has been idle for 
 minutes }

onlinelogs
 [F7] 
 [F8] 
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.004043bf` | `0x4043bf` | 2470 | ✓ |
| `fcn.00409e73` | `0x409e73` | 2219 | ✓ |
| `main` | `0x407452` | 2049 | ✓ |
| `fcn.0040bea2` | `0x40bea2` | 1949 | ✓ |
| `fcn.004086b1` | `0x4086b1` | 1949 | ✓ |
| `fcn.00402c45` | `0x402c45` | 1336 | ✓ |
| `fcn.0040650d` | `0x40650d` | 1147 | ✓ |
| `fcn.0040e8b9` | `0x40e8b9` | 1049 | ✓ |
| `fcn.00406d29` | `0x406d29` | 1030 | ✓ |
| `fcn.0040ca9b` | `0x40ca9b` | 1026 | ✓ |
| `fcn.00406988` | `0x406988` | 929 | ✓ |
| `fcn.004057b6` | `0x4057b6` | 837 | ✓ |
| `fcn.00407e0b` | `0x407e0b` | 837 | ✓ |
| `fcn.00403183` | `0x403183` | 753 | ✓ |
| `fcn.00403d9a` | `0x403d9a` | 733 | ✓ |
| `fcn.0040da55` | `0x40da55` | 716 | ✓ |
| `fcn.00403ae3` | `0x403ae3` | 695 | ✓ |
| `fcn.0040c63f` | `0x40c63f` | 692 | ✓ |
| `fcn.0040d71e` | `0x40d71e` | 635 | ✓ |
| `fcn.0040926a` | `0x40926a` | 628 | ✓ |
| `fcn.0040decb` | `0x40decb` | 616 | ✓ |
| `fcn.00405afb` | `0x405afb` | 600 | ✓ |
| `fcn.004081b7` | `0x4081b7` | 559 | ✓ |
| `fcn.0040f234` | `0x40f234` | 536 | ✓ |
| `fcn.0040bc9b` | `0x40bc9b` | 519 | ✓ |
| `fcn.0040712f` | `0x40712f` | 503 | ✓ |
| `fcn.00409577` | `0x409577` | 500 | ✓ |
| `fcn.00404077` | `0x404077` | 477 | ✓ |
| `fcn.00406339` | `0x406339` | 468 | ✓ |
| `fcn.004022ea` | `0x4022ea` | 458 | ✓ |

### Decompiled Code Files

- [`code/fcn.004022ea.c`](code/fcn.004022ea.c)
- [`code/fcn.00402c45.c`](code/fcn.00402c45.c)
- [`code/fcn.00403183.c`](code/fcn.00403183.c)
- [`code/fcn.00403ae3.c`](code/fcn.00403ae3.c)
- [`code/fcn.00403d9a.c`](code/fcn.00403d9a.c)
- [`code/fcn.00404077.c`](code/fcn.00404077.c)
- [`code/fcn.004043bf.c`](code/fcn.004043bf.c)
- [`code/fcn.004057b6.c`](code/fcn.004057b6.c)
- [`code/fcn.00405afb.c`](code/fcn.00405afb.c)
- [`code/fcn.00406339.c`](code/fcn.00406339.c)
- [`code/fcn.0040650d.c`](code/fcn.0040650d.c)
- [`code/fcn.00406988.c`](code/fcn.00406988.c)
- [`code/fcn.00406d29.c`](code/fcn.00406d29.c)
- [`code/fcn.0040712f.c`](code/fcn.0040712f.c)
- [`code/fcn.00407e0b.c`](code/fcn.00407e0b.c)
- [`code/fcn.004081b7.c`](code/fcn.004081b7.c)
- [`code/fcn.004086b1.c`](code/fcn.004086b1.c)
- [`code/fcn.0040926a.c`](code/fcn.0040926a.c)
- [`code/fcn.00409577.c`](code/fcn.00409577.c)
- [`code/fcn.00409e73.c`](code/fcn.00409e73.c)
- [`code/fcn.0040bc9b.c`](code/fcn.0040bc9b.c)
- [`code/fcn.0040bea2.c`](code/fcn.0040bea2.c)
- [`code/fcn.0040c63f.c`](code/fcn.0040c63f.c)
- [`code/fcn.0040ca9b.c`](code/fcn.0040ca9b.c)
- [`code/fcn.0040d71e.c`](code/fcn.0040d71e.c)
- [`code/fcn.0040da55.c`](code/fcn.0040da55.c)
- [`code/fcn.0040decb.c`](code/fcn.0040decb.c)
- [`code/fcn.0040e8b9.c`](code/fcn.0040e8b9.c)
- [`code/fcn.0040f234.c`](code/fcn.0040f234.c)
- [`code/main.c`](code/main.c)

## Behavioral Analysis

Based on the final disassembly provided in chunk 3/3, the analysis of the malware is updated and expanded. The new code provides significant insight into its **anti-forensics capabilities**, **proactive cleanup routines**, and **sophisticated environment adaptation**.

### Updated Summary
The latest findings confirm that this binary is a highly sophisticated **Remote Access Trojan (RAT)** with a heavy emphasis on "operational security" for the attacker. It doesn't just steal data; it actively works to delete its traces, dynamically adapt to various Windows configurations, and manage multiple concurrent tasks through threading.

---

### Core Functionality & Purpose (Expanded)
*   **Aggressive Evidence Destruction (Anti-Forensics):** 
    *   The function `fcn.00405afb` specifically targets **Mozilla Firefox**. It scans the user's profile directories and, upon finding files like `cookies.sqlite`, it deletes them after they have been processed by other parts of the malware (indicated by the log output "cleared!").
    *   The function `fcn.0040f234` implements a recursive-style cleanup logic. It iterates through file systems, identifies files/directories (potentially its own temporary components), sets them to **Hidden Attributes (`0x80`)**, and then calls `DeleteFileA` or `RemoveDirectoryA`. This ensures that the "footprint" of the infection is purged from the disk.
*   **Dynamic Path Resolution & Environment Mapping:** 
    *   In `fcn.0040712f`, the malware implements a complex system to resolve paths based on environment variables (e.g., `WinDir`, `SystemDrive`, `ProgramFiles`, `AppData`). It doesn't rely on hardcoded strings for everything; instead, it interprets multiple keys (like "Temp" or "UserProfile") and uses `GetLongPathNameA` to construct absolute paths dynamically. This ensures the malware remains functional across different versions of Windows and varied user configurations.
*   **Robust Registry Reconnaissance:**
    *   Function `fcn.00409577` utilizes `RegOpenKeyExA` with a fallback mechanism (checking for "regopened" vs "regmsg"). This indicates the malware is designed to be resilient; if one method of querying system information fails, it attempts an alternative path to ensure it can still collect data for the attacker.
*   **Multi-Threaded Execution Management:**
    *   Function `fcn.004022ea` shows the use of `CreateThread` and `WaitForSingleObject`. This suggests that some malicious tasks (such as the scanning or deletion routines) are spawned in separate threads to prevent the main RAT process from hanging while performing heavy disk I/O, allowing it to maintain a stable connection with the C2 server.

### Suspicious & Malicious Behaviors
*   **Intentional Artifact Masking:** By setting file attributes to "Hidden" before deletion or using `DeleteFileA` immediately after processing browser data, the malware actively hides its presence from both the user and basic automated scans.
*   **Automatic System Mapping:** The sophisticated switch-like logic for handling system paths (WinDir vs SysWOW64) suggests a high level of development intended to target both 32-bit and 64-bit systems effectively.
*   **Information Overload/Collection:** The variety of functions dealing with file lists, directory scanning (`fcn.004081b7`), and system enumeration indicates that the malware is "mapping" the host machine to provide a comprehensive overview to the attacker.

### New Indicators (IOCs) & Behaviors
| Feature | Technique | Purpose |
| :--- | :--- | :--- |
| **Auto-Purge** | `DeleteFileA` / `RemoveDirectoryA` | Removing evidence of dropped files or logs. |
| **Path Mapping** | Dynamic Env Var Resolution | Ensuring maximum compatibility across OS versions. |
| **Attribute Manipulation**| `SetFileAttributesA (0x80)` | Hiding files from the user and basic system views. |
| **Thread Management** | `CreateThread` / `WaitForSingleObject` | Running background tasks without interrupting C2 communication. |
| **Robust Discovery** | Fallback Registry Logic | Ensuring system data is gathered even if primary methods are blocked. |

---

### Final Conclusion of Analysis
The integration of chunk 3/3 confirms that this binary belongs to a high-tier, professional malware family (consistent with the **Remcos** profile). It possesses three distinct layers of sophisticated design:

1.  **Persistence & Stealth:** It doesn't just stay on the system; it actively scrubs itself and its artifacts using automated cleanup routines.
2.  **Operational Flexibility:** It uses dynamic path resolution to ensure it can infect a wide range of targets without needing specific modifications for different Windows environments.
3.  **Robust Infrastructure:** By utilizing multi-threading and fallback logic, it ensures that the "Remote Access" part of the RAT remains stable while it carries out secondary tasks like credential theft and system harvesting.

The malware is engineered to provide an attacker with a long-term, reliable window for surveillance while minimizing the risk of detection by local security tools or manual investigation.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1070.003 | Indicator Removal: File Deletion | The malware utilizes `DeleteFileA` and `RemoveDirectoryA` to purge its own artifacts and browser data from the disk. |
| T1564.003 | Hide Files and Directories | The malware sets file attributes to "Hidden" (0x80) before deletion to mask its presence from users and basic security tools. |
| T1036 | Masquerading | By resolving paths via environment variables instead of hardcoded strings, the malware blends into standard system structures across different OS versions. |
| T1012 | Query Registry | The use of `RegOpenKeyExA` with fallback mechanisms ensures the malware can successfully gather system information even if primary methods are blocked. |
| T1083 | File and Directory Discovery | The analysis identifies dedicated logic for scanning file systems and mapping directories to provide a comprehensive view of the host to the attacker. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs) categorized by type:

### **IP addresses / URLs / Domains**
*   *(None identified in the provided text)*

### **File paths / Registry keys**
*   **Malicious Files/Modules:**
    *   `SbieDll.dll`
    *   `\install.bat`
    *   `\uninstall.bat`
    *   `\update.bat`
*   **Credential & Cookie Theft Paths:**
    *   `\AppData\Local\Google\Chrome\User Data\Default\Login Data` (Chrome Credentials)
    *   `\AppData\Local\Google\Chrome\User Data\Default\Cookies` (Chrome Cookies)
    *   `\key3.db` (Firefox credentials)
    *   `\logins.json` (Firefox credentials)
    *   `\AppData\Roaming\Mozilla\Firefox\Profiles\` (Firefox directory scan)
    *   `\cookies.sqlite` (Firefox cookies)
*   **Registry Keys:**
    *   `Software\Classes\mscfile\shell\open\command`
    *   `Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run\`

### **Mutex names / Named pipes**
*   **Mutex Name:** `Remcos_Mutex_Inj` (Indicates association with the Remcos RAT)

### **Hashes**
*   *(None provided in the source text)*

### **Other artifacts**
*   **C2/Communication Markers:**
    *   `[DataStart]`
    *   `[KeepAlive]`
    *   `Timeout expired, resetting connection.`
*   **Spying & Surveillance Functions (Keywords):**
    *   `playaudio`
    *   `nocamera`
    *   `startcamcap`
    *   `closecam`
    *   `getcamframe`
    *   `initcamcap`
    *   `FreeFrame`
    *   `GetFrame`
    *   `CloseCamera`
    *   `OpenCamera`
    *   `camdlldata`
    *   `camframe`
*   **Anti-Forensics & Detection Evasion:**
    *   `PROMC_WINDOW_CLASS` (Potential check for ProcMon)
    *   `PROCEXPL` (Potential detection of Process Explorer)
    *   `SetFileAttributesA (0x80)` (Used to set file attributes to 'Hidden' before deletion)
    *   `HARDWARE\ACPI\DSDT\VBOX__` (Check for VirtualBox/Virtualization environments)

---
**Analyst Note:** The presence of the string `Remcos_Mutex_Inj` and the specific sequence of credential theft paths confirm this is a variant of the **Remcos Remote Access Trojan**. The inclusion of camera-related functions and "KeepAlive" signaling indicates active spying and persistent C2 communication capabilities.

---

## Malware Family Classification

1. **Malware family**: Remcos
2. **Malware type**: RAT
3. **Confidence**: High
4. **Key evidence**: 
    * **Specific Indicators:** The presence of the unique mutex `Remcos_Mutex_Inj` and explicit analyst notes identifying it as a Remcos variant.
    * **Spyware & Remote Access Capabilities:** Inclusion of multiple camera-related functions (e.g., `startcamcap`, `getcamframe`, `initcamcap`) and "KeepAlive" signaling for stable C2 communication.
    * **Advanced Anti-Forensics:** Sophisticated tactics including automatic deletion of files, setting attributes to "Hidden" before cleanup, and dynamic path resolution to ensure cross-environment compatibility.
