# Threat Analysis Report

**Generated:** 2026-08-15 20:54 UTC
**Sample:** `0f47be922777d7d7fb8e6ce5076deb4a4ca03f28b9f80e74adc6f50d4e23e1d7_0f47be922777d7d7fb8e6ce5076deb4a4ca03f28b9f80e74adc6f50d4e23e1d7.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0f47be922777d7d7fb8e6ce5076deb4a4ca03f28b9f80e74adc6f50d4e23e1d7_0f47be922777d7d7fb8e6ce5076deb4a4ca03f28b9f80e74adc6f50d4e23e1d7.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386 (stripped to external PDB), 4 sections |
| Size | 91,364 bytes |
| MD5 | `d46aa12c03579e67390f41b88e3f4f7f` |
| SHA1 | `2180c5adb074bc56ecfc84eae564142bc5850394` |
| SHA256 | `0f47be922777d7d7fb8e6ce5076deb4a4ca03f28b9f80e74adc6f50d4e23e1d7` |
| Overall entropy | 4.422 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1328362256 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.nsp0` | 33,792 | 4.077 | No |
| `.nsp1` | 12,800 | 7.881 | ⚠️ Yes |
| `.nsp2` | 0 | 0.0 | No |
| `.imports` | 1,536 | 3.625 | No |

### Imports

**ADVAPI32.DLL**: `RegSetValueExA`, `RegQueryValueExA`, `RegOpenKeyExA`, `RegCreateKeyA`, `RegOpenKeyA`, `RegCloseKey`
**KERNEL32.DLL**: `GetStringTypeA`, `LCMapStringW`, `WaitForSingleObject`, `CreateThread`, `HeapFree`, `DeleteFileA`, `ExitProcess`, `lstrcmpiA`, `lstrcatA`, `GetWindowsDirectoryA`, `HeapAlloc`, `GetProcessHeap`, `Sleep`, `GetModuleFileNameA`, `CloseHandle`
**USER32.DLL**: `wsprintfA`
**WININET.DLL**: `InternetOpenA`, `InternetSetOptionExA`, `InternetOpenUrlA`, `InternetCloseHandle`, `InternetReadFile`
**IPHLPAPI.DLL**: `GetAdaptersInfo`

## Extracted Strings

Total strings found: **294** (showing first 100)

```
!This program cannot be run in DOS mode.
$
.imports
D$8h\a@
D$,X`@
D$8X`@
T$\PQj
D$(RVWP
D$RPQ
D$RPQ
QQSVWd
t.;t$$t(
sO;>|C;~
VC20XC00U
YYh(`@
;t$s
HHtYHHtF
tPhtT@
runtime error 
TLOSS error

SING error

DOMAIN error

R6028
- unable to initialize heap

R6027
- not enough space for lowio initialization

R6026
- not enough space for stdio initialization

R6025
- pure virtual function call

R6024
- not enough space for _onexit/atexit table

R6019
- unable to open console device

R6018
- unexpected heap error

R6017
- unexpected multithread lock error

R6016
- not enough space for thread data


abnormal program termination

R6009
- not enough space for environment

R6008
- not enough space for arguments

R6002
- floating point not loaded

Microsoft Visual C++ Runtime Library
Runtime Error!

Program: 
<program name unknown>
GetLastActivePopup
GetActiveWindow
MessageBoxA
user32.dll
%s?mac=%02X-%02X-%02X-%02X-%02X-%02X
Accept: */*
Content-Type: application/x-www-form-urlencoded
Accept-Language: zh-cn
Connection: Keep-Alive

Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; CIBA; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022)
pomdfghrt
\microsofthelp.exe
WindowsHookExON
HidePlugin.dll
microsofthelp
Software\Microsoft\Windows\CurrentVersion\Run
C:\Program Files\Internet Explorer
iexplore.exe
Shell32.dll
ShellExecuteExA
Software\motherFucker
GetStringTypeALCMapStringWWaitForSingleObjectCreateThreadHeapFreeDeleteFileAExitProcesslstrcmpiAlstrcatAGetWindowsDirectoryAHeapAllocGetProcessHeapSleepGetModuleFileNameACloseHandleGetLastErrorCreateMutexAGetProcAddressLoadLibraryAHeapReAllocGetTickCountFindCloseFindFirstFileATerminateProcessCreateProcessACreateFileAReadFileWriteFileFlushFileBuffersGetFileSizeLCMapStringAGetStringTypeWMultiByteToWideCharGetOEMCPGetACPGetCPInfoRtlUnwindSetUnhandledExceptionFilterIsBadReadPtrIsBadWritePtrIsBadCodePtrGetCurrentProcessGetStdHandleWideCharToMultiByteRegSetValueExARegQueryValueExARegOpenKeyExARegCreateKeyARegOpenKeyARegCloseKeyGetAdaptersInfoInternetOpenAInternetSetOptionExAInternetOpenUrlAInternetCloseHandleInternetReadFilewsprintfA
KERNEL32.DLL
ADVAPI32.DLL
IPHLPAPI.DLL
WININET.DLL
USER32.DLL
LoadLibraryA
GetProcAddress
VirtualProtect
VirtualAlloc
VirtualFree
ExitProcess
RegSetValueExA
GetAdaptersInfo
InternetOpenA
wsprintfA
VA1^K"
y~,vU
9M`U`
sNbUdD
@@9A	@J
U,.-.._
$ns+'A
W|hE
ap+
2|"dGD
;jZ!IC=9
Qmo$SA
1"{>|:u
zA7I--m
GkA$VL
ADxwfC
I~7Cq=
O=`]N;
c[1f!EY
uEc(ykW
,[$Yx/@_
ADVAPI32.DLL
RegSetValueExA
RegQueryValueExA
RegOpenKeyExA
RegCreateKeyA
RegOpenKeyA
RegCloseKey
KERNEL32.DLL
GetStringTypeA
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00402cbc` | `0x402cbc` | 1568 | ✓ |
| `entry0` | `0x401000` | 1176 | ✓ |
| `fcn.00402f90` | `0x402f90` | 821 | ✓ |
| `fcn.0040423f` | `0x40423f` | 548 | ✓ |
| `fcn.0040a2a2` | `0x40a2a2` | 533 | ✓ |
| `fcn.00402a16` | `0x402a16` | 440 | ✓ |
| `fcn.00402505` | `0x402505` | 423 | ✓ |
| `fcn.0040395b` | `0x40395b` | 409 | ✓ |
| `fcn.00401660` | `0x401660` | 402 | ✓ |
| `fcn.00403b9a` | `0x403b9a` | 389 | ✓ |
| `fcn.00401810` | `0x401810` | 364 | ✓ |
| `fcn.00403512` | `0x403512` | 339 | ✓ |
| `fcn.0040448e` | `0x40448e` | 329 | ✓ |
| `fcn.004033a0` | `0x4033a0` | 301 | ✓ |
| `fcn.00401560` | `0x401560` | 254 | ✓ |
| `fcn.004037e0` | `0x4037e0` | 254 | ✓ |
| `fcn.00401ac0` | `0x401ac0` | 249 | ✓ |
| `fcn.004036f0` | `0x4036f0` | 240 | ✓ |
| `fcn.0040bfeb` | `0x40bfeb` | 227 | ✓ |
| `fcn.00401ec0` | `0x401ec0` | 223 | ✓ |
| `fcn.004021d6` | `0x4021d6` | 180 | ✓ |
| `fcn.0040a4b7` | `0x40a4b7` | 170 | ✓ |
| `fcn.004026ac` | `0x4026ac` | 168 | ✓ |
| `fcn.0040a561` | `0x40a561` | 159 | ✓ |
| `fcn.004027b1` | `0x4027b1` | 158 | ✓ |
| `fcn.004028e0` | `0x4028e0` | 156 | ✓ |
| `fcn.0040246a` | `0x40246a` | 155 | ✓ |
| `fcn.004032ed` | `0x4032ed` | 153 | ✓ |
| `fcn.00403665` | `0x403665` | 137 | ✓ |
| `fcn.00402e20` | `0x402e20` | 132 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.00401560.c`](code/fcn.00401560.c)
- [`code/fcn.00401660.c`](code/fcn.00401660.c)
- [`code/fcn.00401810.c`](code/fcn.00401810.c)
- [`code/fcn.00401ac0.c`](code/fcn.00401ac0.c)
- [`code/fcn.00401ec0.c`](code/fcn.00401ec0.c)
- [`code/fcn.004021d6.c`](code/fcn.004021d6.c)
- [`code/fcn.0040246a.c`](code/fcn.0040246a.c)
- [`code/fcn.00402505.c`](code/fcn.00402505.c)
- [`code/fcn.004026ac.c`](code/fcn.004026ac.c)
- [`code/fcn.004027b1.c`](code/fcn.004027b1.c)
- [`code/fcn.004028e0.c`](code/fcn.004028e0.c)
- [`code/fcn.00402a16.c`](code/fcn.00402a16.c)
- [`code/fcn.00402cbc.c`](code/fcn.00402cbc.c)
- [`code/fcn.00402e20.c`](code/fcn.00402e20.c)
- [`code/fcn.00402f90.c`](code/fcn.00402f90.c)
- [`code/fcn.004032ed.c`](code/fcn.004032ed.c)
- [`code/fcn.004033a0.c`](code/fcn.004033a0.c)
- [`code/fcn.00403512.c`](code/fcn.00403512.c)
- [`code/fcn.00403665.c`](code/fcn.00403665.c)
- [`code/fcn.004036f0.c`](code/fcn.004036f0.c)
- [`code/fcn.004037e0.c`](code/fcn.004037e0.c)
- [`code/fcn.0040395b.c`](code/fcn.0040395b.c)
- [`code/fcn.00403b9a.c`](code/fcn.00403b9a.c)
- [`code/fcn.0040423f.c`](code/fcn.0040423f.c)
- [`code/fcn.0040448e.c`](code/fcn.0040448e.c)
- [`code/fcn.0040a2a2.c`](code/fcn.0040a2a2.c)
- [`code/fcn.0040a4b7.c`](code/fcn.0040a4b7.c)
- [`code/fcn.0040a561.c`](code/fcn.0040a561.c)
- [`code/fcn.0040bfeb.c`](code/fcn.0040bfeb.c)

## Behavioral Analysis

This analysis is based on the provided strings and decompiled code from the binary sample.

### Core Functionality and Purpose
The binary appears to be a **malware loader or "dropper"** designed to establish a foothold on a system, perform initial reconnaissance (information gathering), and communicate with a remote Command & Control (C2) server. It uses several techniques to hide its true actions from basic security scanners.

### Suspicious and Malicious Behavs
*   **Persistence Mechanism:** The presence of the string `Software\Microsoft\Windows\CurrentVersion\Run` indicates that the malware attempts to modify Windows Registry keys to ensure it automatically starts every time the user logs in. 
*   **Command & Control (C2) Communication:**
    *   The code imports and uses `WinINet` functions (`InternetOpenA`, `InternetSetOptionExA`, `InternetOpenUrlA`, `InternetReadFile`).
    *   The inclusion of standard HTTP headers (e.g., `User-Agent`, `Content-Type`, `Accept`) indicates it is designed to blend in with normal web traffic while communicating with a remote server.
*   **Information Gathering:** 
    *   The use of `GetAdaptersInfo` suggests the malware is collecting local network information, such as the machine's **MAC address**. This is often used by attackers to uniquely identify a victim's device within a campaign.
    *   A specific format string for a MAC address (`%s?mac=%02X-%02X-...`) confirms this intent.
*   **Data Deobfuscation/Decryption:** 
    *   The code contains an explicit **XOR loop** used to decrypt data in memory (seen in the logic calculating `iVar16` and looping through a buffer). This is a classic technique to hide strings, IP addresses, or subsequent stages of malicious code from static analysis.
*   **Masquerading:** 
    *   The binary contains several strings that appear to mimic legitimate system files or services (e.g., `microsofthelp.exe`, `HidePlugin.dll`). This is a common technique to mislead both the user and automated security tools.
    *   Conversely, some internal identifiers are "loud" and clearly malicious (e.g., `Software\motherFucker`), which may be used for internal tracking by the threat actor.

### Notable Techniques & Patterns
*   **Dynamic API Loading:** The code uses `GetProcAddress` and `LoadLibraryA`. This allows the malware to resolve its intended functions at runtime, making it harder for analysts to see what capabilities it has just by looking at the Import Address Table (IAT).
*   **Anti-Analysis/Evasion (Timing):** There is evidence of a "wait" or sleep loop (`(**0x40504c)(iVar16 * 60000)`), which suggests the malware waits for a significant amount of time after certain actions to bypass automated sandbox analysis that usually only monitors behavior for a few minutes.
*   **Execution of Remote/Dropped Files:** The extensive list of local file paths (some containing `.virus.exe` or hidden in `\AppData\Local\Temp\`) suggests the loader is designed to drop and execute additional payloads on the system.
*   **Multi-Step Execution:** The use of `CreateThread` to launch a new thread for specific tasks (like communication) indicates the malware may perform multiple actions concurrently or isolate different behaviors into separate threads.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1547.001 | Boot or Logon Autostart Execution: Registry Run Keys | The malware modifies the `Run` registry key to ensure persistence and automatic execution upon user login. |
| T1071.001 | Application Layer Protocol: Web Protocols | The use of `WinINet` and standard HTTP headers indicates an attempt to blend C2 communications with legitimate web traffic. |
| T1016 | System Network Configuration Discovery | The use of `GetAdaptersInfo` to retrieve MAC addresses is used to gather network information for identifying unique victim devices. |
| T1027 | Obfuscated Files or Information | An XOR loop is utilized to decrypt data in memory, hiding malicious strings and configuration details from static analysis. |
| T1036 | Masquerading | The use of file names like `microsofthelp.exe` mimics legitimate system files to deceive users and security tools. |
| T1036 | Masquerading | The use of `GetProcAddress` and `LoadLibraryA` hides the malware's functional capabilities from analysis by not populating the Import Address Table (IAT). |
| T1497* | (Defense Evasion: Timing) | A "wait" loop is used to stall execution, which is a common tactic to bypass time-limited sandbox environments. |

*\*Note: While T1497 specifically refers to System Shutdown in current MITRE documentation, it was historically associated with various timing behaviors; however, the behavior described is most accurately categorized under broader "Defense Evasion" strategies involving delayed execution.*

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs) categorized by type:

### **IP addresses / URLs / Domains**
*Note: No explicit IP addresses or raw domains were found in the strings; however, a C2 data structure was identified.*
*   **C2 Data Pattern:** `%s?mac=%02X-%02X-%02X-%02X-%02X-%02X` (Used to transmit the machine's MAC address to the remote server).

### **File paths / Registry keys**
**Registry Keys:**
*   `Software\motherFucker` (Malicious indicator)
*   `Software\Microsoft\Windows\CurrentVersion\Run` (Persistence mechanism)

**Files / Paths:**
*   `microsofthelp.exe`
*   `HidePlugin.dll`
*   `C:\Users\Frank\Desktop\YRFFICmC.exe`
*   `C:\Users\admin\Downloads\6c17ab9ee385192357d5739d1df6b7c4.virus.exe`
*   `C:\Users\admin\Downloads\96216416b1505c5768f043e7dff88fb5.virus.exe`
*   `C:\Users\george\Desktop\software.exe`
*   `C:\Users\maxine\AppData\Local\Temp\file.exe`
*   `C:\Users\maxine\AppData\Local\Temp\K504LACUAIEXUOCQLF0K2RUS.exe`
*   `C:\Users\Steve\AppData\Local\Temp\21b9b5ee90f8e9353b92.exe`
*   `C:\Users\Steve\AppData\Local\Temp\75b2ac0ac1b1b7eb5bc1.exe`
*   `C:\Users\Steve\AppData\Local\Temp\bc93b82b247bf0c304aa.exe`
*   `C:\Users\azure\Downloads\microsofthelp.exe`
*   `C:\Users\azure\Downloads\5cb6f5ac3f2c1f63c5aa51265b1d94dc841fae49631373c9eee2461d056d93f5.exe`
*   `C:\Users\azure\Downloads\1adf8371c2d5cbffa2184cdf97d94a6f1e6268654ac60bd4f872dd2c5eaa4c1f.exe`
*   `C:\feZfHXUW.exe`
*   `C:\7lFDA44i.exe`

### **Mutex names / Named pipes**
*None identified.*

### **Hashes**
*Note: While several long hexadecimal strings were found in the file paths (e.g., `C:\221f2d56...`), these appear to be randomly generated filenames rather than standard MD5/SHA hashes of known files.*

### **Other artifacts**
**User Agents:**
*   `Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; CIBA; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022)`

**C2 / Network Patterns:**
*   `Content-Type: application/x-www-form-urlencoded`
*   `Accept-Language: zh-cn`
*   `Connection: Keep-Alive`

---

## Malware Family Classification

**1. Malware family:** Unknown (Potential custom loader)
**2. Malware type:** Dropper / Loader
**3. Confidence:** High

**4. Key evidence:**
*   **Multi-Stage Delivery & Persistence:** The malware employs classic "dropper" behavior by utilizing registry persistence (`Run` key), masquerading as system files (e.g., `microsofthelp.exe`), and using a list of diverse file paths to deploy additional components/payloads.
*   **Evasion & Obfuscation:** The presence of an XOR decryption loop, dynamic API loading (`GetProcAddress`/`LoadLibraryA`), and long "sleep" timers specifically designed to bypass automated sandbox analysis indicates a deliberate effort to hide the primary malicious payload from security researchers.
*   **C2 Communication & Reconnaissance:** The use of `WinINet` for HTTP communication combined with `GetAdaptersInfo` to harvest MAC addresses confirms its role as an initial access tool, intended to identify unique machines and establish a stable connection to a remote server.
