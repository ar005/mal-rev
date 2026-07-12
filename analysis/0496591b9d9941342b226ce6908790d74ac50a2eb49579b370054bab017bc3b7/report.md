# Threat Analysis Report

**Generated:** 2026-07-11 20:08 UTC
**Sample:** `0496591b9d9941342b226ce6908790d74ac50a2eb49579b370054bab017bc3b7_0496591b9d9941342b226ce6908790d74ac50a2eb49579b370054bab017bc3b7.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0496591b9d9941342b226ce6908790d74ac50a2eb49579b370054bab017bc3b7_0496591b9d9941342b226ce6908790d74ac50a2eb49579b370054bab017bc3b7.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386 (stripped to external PDB), 3 sections |
| Size | 103,863 bytes |
| MD5 | `39b05a25bbb5096ce57e941b340ef75b` |
| SHA1 | `68705cb5ff0826146dc7b93c85192ecd4980025d` |
| SHA256 | `0496591b9d9941342b226ce6908790d74ac50a2eb49579b370054bab017bc3b7` |
| Overall entropy | 3.482 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1326947327 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.MPRESS1` | 46,592 | 5.036 | No |
| `.MPRESS2` | 1,024 | 5.972 | No |
| `.imports` | 1,536 | 3.605 | No |

### Imports

**ADVAPI32.dll**: `RegSetValueExA`, `RegQueryValueExA`, `RegOpenKeyExA`, `RegCreateKeyA`, `RegOpenKeyA`, `RegCloseKey`
**KERNEL32.dll**: `GetStringTypeA`, `LCMapStringW`, `WaitForSingleObject`, `CreateThread`, `HeapFree`, `DeleteFileA`, `ExitProcess`, `lstrcmpiA`, `lstrcatA`, `GetWindowsDirectoryA`, `HeapAlloc`, `GetProcessHeap`, `Sleep`, `GetModuleFileNameA`, `CloseHandle`
**USER32.dll**: `wsprintfA`
**WININET.dll**: `InternetOpenA`, `InternetSetOptionExA`, `InternetOpenUrlA`, `InternetCloseHandle`, `InternetReadFile`
**iphlpapi.dll**: `GetAdaptersInfo`

## Extracted Strings

Total strings found: **432** (showing first 100)

```
!Win32 .EXE.
$@
.MPRESS1
.MPRESS2
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
kernel32.dll
LoadLibraryA
GetProcAddress
VirtualAlloc
VirtualFree
DS	_a
_dmIspH
6.1{>G
yNv.*|3
gK &O?z
c7tC0'
BL
3
\uI9(V
V_YZ-y
bIhgJ.
+%(JVx!cK
R&|?pc\

9X,[<;PCd
Z(}1B,
X,@ m
Q
>(I>@}
H2Ujh5
cX}C:$
ecqoX,
HXp,`{
{Z4*eXS
z7B'!Z
=MVXf)C
NR30*wU
nB%tG2@A
ADVAPI32.dll
RegSetValueExA
RegQueryValueExA
RegOpenKeyExA
RegCreateKeyA
RegOpenKeyA
RegCloseKey
iphlpapi.dll
GetAdaptersInfo
KERNEL32.dll
GetStringTypeA
LCMapStringW
WaitForSingleObject
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00402c6c` | `0x402c6c` | 1568 | ✓ |
| `fcn.00401058` | `0x401058` | 1002 | ✓ |
| `fcn.00402f40` | `0x402f40` | 821 | ✓ |
| `fcn.0040d154` | `0x40d154` | 671 | ✓ |
| `fcn.004041ef` | `0x4041ef` | 548 | ✓ |
| `fcn.0040d1e2` | `0x40d1e2` | 524 | ✓ |
| `fcn.004029c6` | `0x4029c6` | 440 | ✓ |
| `fcn.004024b5` | `0x4024b5` | 423 | ✓ |
| `fcn.0040390b` | `0x40390b` | 409 | ✓ |
| `fcn.00401610` | `0x401610` | 402 | ✓ |
| `fcn.00403b4a` | `0x403b4a` | 389 | ✓ |
| `fcn.004017c0` | `0x4017c0` | 364 | ✓ |
| `fcn.004034c2` | `0x4034c2` | 339 | ✓ |
| `fcn.0040443e` | `0x40443e` | 329 | ✓ |
| `fcn.00403350` | `0x403350` | 301 | ✓ |
| `fcn.0040909d` | `0x40909d` | 270 | ✓ |
| `fcn.00401510` | `0x401510` | 254 | ✓ |
| `fcn.00403790` | `0x403790` | 254 | ✓ |
| `fcn.00401a70` | `0x401a70` | 249 | ✓ |
| `fcn.004036a0` | `0x4036a0` | 240 | ✓ |
| `fcn.00401e70` | `0x401e70` | 223 | ✓ |
| `fcn.00402186` | `0x402186` | 180 | ✓ |
| `fcn.0040265c` | `0x40265c` | 168 | ✓ |
| `fcn.00402761` | `0x402761` | 158 | ✓ |
| `fcn.00402890` | `0x402890` | 156 | ✓ |
| `fcn.0040241a` | `0x40241a` | 155 | ✓ |
| `fcn.0040329d` | `0x40329d` | 153 | ✓ |
| `fcn.00403615` | `0x403615` | 137 | ✓ |
| `fcn.00402dd0` | `0x402dd0` | 132 | ✓ |
| `fcn.00401d30` | `0x401d30` | 131 | ✓ |

### Decompiled Code Files

- [`code/fcn.00401058.c`](code/fcn.00401058.c)
- [`code/fcn.00401510.c`](code/fcn.00401510.c)
- [`code/fcn.00401610.c`](code/fcn.00401610.c)
- [`code/fcn.004017c0.c`](code/fcn.004017c0.c)
- [`code/fcn.00401a70.c`](code/fcn.00401a70.c)
- [`code/fcn.00401d30.c`](code/fcn.00401d30.c)
- [`code/fcn.00401e70.c`](code/fcn.00401e70.c)
- [`code/fcn.00402186.c`](code/fcn.00402186.c)
- [`code/fcn.0040241a.c`](code/fcn.0040241a.c)
- [`code/fcn.004024b5.c`](code/fcn.004024b5.c)
- [`code/fcn.0040265c.c`](code/fcn.0040265c.c)
- [`code/fcn.00402761.c`](code/fcn.00402761.c)
- [`code/fcn.00402890.c`](code/fcn.00402890.c)
- [`code/fcn.004029c6.c`](code/fcn.004029c6.c)
- [`code/fcn.00402c6c.c`](code/fcn.00402c6c.c)
- [`code/fcn.00402dd0.c`](code/fcn.00402dd0.c)
- [`code/fcn.00402f40.c`](code/fcn.00402f40.c)
- [`code/fcn.0040329d.c`](code/fcn.0040329d.c)
- [`code/fcn.00403350.c`](code/fcn.00403350.c)
- [`code/fcn.004034c2.c`](code/fcn.004034c2.c)
- [`code/fcn.00403615.c`](code/fcn.00403615.c)
- [`code/fcn.004036a0.c`](code/fcn.004036a0.c)
- [`code/fcn.00403790.c`](code/fcn.00403790.c)
- [`code/fcn.0040390b.c`](code/fcn.0040390b.c)
- [`code/fcn.00403b4a.c`](code/fcn.00403b4a.c)
- [`code/fcn.004041ef.c`](code/fcn.004041ef.c)
- [`code/fcn.0040443e.c`](code/fcn.0040443e.c)
- [`code/fcn.0040909d.c`](code/fcn.0040909d.c)
- [`code/fcn.0040d154.c`](code/fcn.0040d154.c)
- [`code/fcn.0040d1e2.c`](code/fcn.0040d1e2.c)

## Behavioral Analysis

Based on the provided disassembly and string data, this binary exhibits characteristics of a **malware sample**, likely a Trojan or a Downloader. It includes features for persistence, network communication (exfiltration/command & control), and evasive maneuvers.

### Core Functionality and Purpose
The primary purpose of this code appears to be establishing a foothold on a system and communicating with a remote server. 
*   **Data Gathering:** The inclusion of `GetAdaptersInfo` and specialized format strings (likely for MAC addresses or unique hardware IDs) suggests it collects machine information.
*   **Persistence:** It actively interacts with the Windows Registry to ensure it runs automatically on startup.
*   **Resource Retrieval/Communication:** It uses the WinINet API to connect to remote URLs, likely to download additional modules or send stolen data to a command-and-control (C2) server.

### Suspicious and Malicious Behaviors
The following behaviors are highly indicative of malicious intent:

*   **Persistence Mechanism:** 
    *   The string `Software\Microsoft\Windows\CurrentVersion\Run` confirms the program attempts to register itself in the Windows "Run" key, ensuring it survives a system reboot.
*   **Network Communication (C2/Exfiltration):** 
    *   The code utilizes `WinINet.dll` functions (`InternetOpenA`, `InternetSetOptionExA`, `InternetOpenUrlA`, `InternetReadFile`). 
    *   The presence of HTTP header strings (e.g., `Content-Type: application/x-www-form-urlencoded`) indicates the construction of web requests to a remote server.
*   **Process Manipulation:** 
    *   Usage of `CreateThread` and `WaitForSingleObject` suggests the program spawns multiple threads to perform tasks (like networking or hidden operations) while keeping the main process alive or "waiting" for completion.
    *   The use of `TerminateProcess` in function `fcn.00401d30` is often used by malware to terminate child processes once a specific task is completed to avoid detection.
*   **Anti-Analysis/Evasion:**
    *   **Delayed Execution:** Frequent calls to `Sleep()` (seen in `fcn.00401058`) are classic techniques to bypass automated "sandboxes" that only monitor behavior for a short window of time.
    *   **Dynamic API Resolution:** The code uses `LoadLibraryA` and `GetProcAddress` frequently (e.g., `fcn.00401510`, `fcn.00403615`). This is used to call functions whose names are not listed in the Import Address Table (IAT), making static analysis more difficult.
    *   **Self-Modification/Hidden Logic:** The logic involving large loops and bitwise operations (e.g., `fcn.00401058`) suggests the decryption of a payload or data buffer at runtime.

### Notable Techniques and Patterns
*   **Masquerading:** The inclusion of strings like `microsofthelp.exe` and `HidePlugin.dll`, combined with the registry path for "motherFucker" (a common crude tactic in older malware families), suggests an attempt to hide its true purpose behind familiar or distracting names.
*   **Hidden Payload Loading:** The structure of functions like `fcn.00401510` and `fcn.00403615` indicates that the binary likely "drops" or loads additional DLLs into memory to perform its primary malicious payload, a common tactic in multi-stage infections.
*   **Information Stealing:** The presence of `GetAdaptorInfo` (networking details) and custom formatting for MAC addresses strongly suggests it is collecting unique identifier data from the victim's machine.

### Summary Conclusion
This binary is **malicious**. It is designed to establish a persistent foothold on a Windows system, gather local information about the device, and communicate with an external server via HTTP/HTTPS. The inclusion of anti-analysis techniques like `Sleep` loops and dynamic API resolution indicates it was crafted to evade security products and manual analysis.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1547.001** | Boot or Logon Autostart Execution: Registry Run Keys/Startup Folder | The malware specifically targets the `Software\Microsoft\Windows\CurrentVersion\Run` registry key to ensure it persists after a system reboot. |
| **T1071.001** | Application Layer Protocol: Web Protocols | The use of the WinINet library (`InternetOpenUrlA`, etc.) and HTTP header strings indicates that the malware communicates with its C2 server over standard web protocols. |
| **T1497** | Virtualization/Sandbox Evasion | The frequent use of `Sleep()` calls is a documented tactic used to delay execution until after a sandbox's analysis window has expired. |
| **T1036** | Masquerading | The binary uses deceptive naming conventions (e.g., `microsofthelp.exe` and `HidePlugin.dll`) to blend in with legitimate system files and mislead investigators. |
| **T1027** | Obfuscated Valid Ports | While the analysis notes "Dynamic API Resolution," this behavior is a common technique used to hide functionality from static analysis by resolving functions at runtime rather than listing them in the IAT. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *(None identified in the provided text; while network activity is described, no specific IP addresses or domain names were present.)*

**File paths / Registry keys**
*   `Software\Microsoft\Windows\CurrentVersion\Run` (Persistence mechanism)
*   `Software\motherFucker` (Suspicious/Malicious registry key)
*   `\microsofthelp.exe` (Potential masqueraded executable)
*   `HidePlugin.dll` (Identified malicious DLL)

**Mutex names / Named pipes**
*   *(None identified)*

**Hashes**
*   *(None identified in the provided strings)*

**Other artifacts**
*   **User-Agent String:** `Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; CIBA; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022)`
*   **HTTP Header Pattern:** `Content-Type: application/x-www-form-urlencoded` (Used for C2 communication)
*   **Information Gathering Pattern:** `%s?mac=%02X-%02X-%02X-%02X-%02X-%02X-%02X` (Specific format string used to capture and format MAC addresses)
*   **Masquerading Keywords:** `microsofthelp`, `HidePlugin`

---

## Malware Family Classification

1. **Malware family**: Trojan / Downloader
2. **Malware type**: Loader
3. **Confidence**: High

4. **Key evidence**:
*   **Multi-Stage Execution:** The use of `WinINet` functions to communicate with remote servers, combined with the extraction of machine identifiers (MAC addresses), indicates a "Loader" role where the primary binary is designed to establish a foothold and fetch subsequent malicious modules.
*   **Evasion Tactics:** The presence of `Sleep()` loops for sandbox evasion, Dynamic API Resolution (`GetProcAddress`/`LoadLibrary`) to hide functionality from static analysis, and the masquerading of filenames (e.g., `microsofthelp.exe`) are hallmark traits of sophisticated loaders.
*   **Persistence & Stealth:** The malware explicitly modifies the Windows "Run" registry key for persistence and employs process manipulation (such as using `TerminateProcess` on child processes) to hide its activity from the user and security tools.
