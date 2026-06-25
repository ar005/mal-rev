# Threat Analysis Report

**Generated:** 2026-06-24 16:03 UTC
**Sample:** `0081d6ef697668923ef8e36ee6b463a194044ad75ae6e9dd74f36ebed2298167_0081d6ef697668923ef8e36ee6b463a194044ad75ae6e9dd74f36ebed2298167.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0081d6ef697668923ef8e36ee6b463a194044ad75ae6e9dd74f36ebed2298167_0081d6ef697668923ef8e36ee6b463a194044ad75ae6e9dd74f36ebed2298167.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386 (stripped to external PDB), 3 sections |
| Size | 128,246 bytes |
| MD5 | `9b3c8beee85e09ce0e7ca7d3ce852ec9` |
| SHA1 | `5a8b3c4110a3d0d94d69122b3316efa752eeb0de` |
| SHA256 | `0081d6ef697668923ef8e36ee6b463a194044ad75ae6e9dd74f36ebed2298167` |
| Overall entropy | 3.093 |
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

Total strings found: **526** (showing first 100)

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

Based on the analysis of the provided strings and decompiled code, this binary is a **downloader/dropper** designed to establish persistence on a system and fetch additional payloads from a remote server.

### Core Functionality
The primary purpose of this code is to act as an initial infection vector. It establishes a foothold by modifying registry keys for automatic execution and then uses the Windows Internet (WinINET) library to reach out to a web server, download data (likely a secondary malicious payload), and potentially execute it.

### Suspicious and Malicious Behaviors

*   **Persistence Mechanism:**
    *   The code contains specific logic to interact with registry keys. The strings confirm the use of `Software\Microsoft\Windows\CurrentVersion\Run`, which is a classic technique used by malware to ensure the program automatically starts every time the user logs in.
    *   A highly suspicious (and non-standard) registry key, `Software\motherFucker`, is present, indicating a malicious intent or specific naming convention for unauthorized configuration.

*   **Network Communication:**
    *   The code utilizes the `WININET` library (`InternetOpenA`, `InternetSetOptionExA`, `InternetOpenUrlA`). These are used to connect to remote servers and retrieve data from URLs. 
    *   The presence of standard HTTP headers in the strings (e.g., `Content-Type: application/x-www-form-urlencoded`) suggests it is prepared to communicate with web servers using standard protocols, potentially masking its traffic as legitimate web requests.

*   **Dropper/Downloader Behavior:**
    *   Function `fcn.004017c0` specifically handles opening a URL, reading the content into a memory buffer (`InternetReadFile`), and managing that memory via `HeapAlloc`/`HeapReAlloc`. This is a classic pattern for downloading "payloads" (like executables or scripts) from the internet.

*   **Anti-Analysis & Evasion:**
    *   The code utilizes multiple `Sleep()` calls within loops while checking conditions. This is a common technique to delay execution, which can bypass automated sandboxes that only monitor a sample for a few seconds/minutes.
    *   It uses dynamic API resolution (`GetProcAddress` and `LoadLibraryA`). Instead of calling functions directly (which would show up easily in an import table), it resolves them at runtime to hide its capabilities from basic static analysis tools.

*   **Masquerading:**
    *   The inclusion of strings like "microsofthelp" and references to `iexplore.exe` suggests the malware may attempt to masquerade as a legitimate system utility or a browser update/helper tool to deceive the user during the infection process.

### Notable Techniques & Patterns
*   **WinINet Implementation:** The heavy reliance on the WinINET library is common in Windows-based malware for fetching remote configurations or second-stage binaries.
*   **Dynamic Memory Management:** The code performs manual heap management for buffers received over the network, indicating it can handle large amounts of data (like an entire EXE file) transferred from a remote server.
*   **Persistence via Registry:** The use of the "Run" key is one of the most common and reliable ways for malware to maintain access on a compromised Windows machine.
*   **Reflective-style loading indicators:** The combination of `VirtualAlloc`, `GetProcAddress`, and `LoadLibrary` often points toward a routine used to load and execute code in memory rather than saving it to disk, which helps evade signature-based antivirus detections.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1547.001 | Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder | The malware utilizes the `Software\Microsoft\Windows\CurrentVersion\Run` key to ensure it executes automatically upon user login. |
| T1105 | Ingress Tool Transfer | The code leverages the WinINet library and specific functions like `InternetReadFile` to download secondary payloads from a remote server. |
| T1497 | Virtualization/Sandbox Detection | The use of multiple `Sleep()` calls within loops is a standard technique used to stall execution and evade detection by automated, time-limited sandbox environments. |
| T1637 | Reflective Code Loading | The combination of `VirtualAlloc`, `GetProcAddress`, and `LoadLibrary` indicates the malware's intent to load and execute code directly in memory to bypass signature-based security. |
| T1027 | Weak Passwords (No, wait - Incorrect mapping) | *Correction:* **T1129** (System Services) is often used for dynamic resolution, but more accurately, the behavior of utilizing `GetProcAddress` to hide API imports is a core component of the **Reflective Code Loading (T1637)** and evasion tactics. |

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral reports, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *(None identified in the provided text)*

**File paths / Registry keys**
*   `\microsofthelp.exe` (Suspicious executable name used for masquerading)
*   `HidePlugin.dll` (Non-standard DLL potentially used for malicious functionality)
*   `Software\motherFucker` (Non-standard, high-confidence malicious registry key)

**Mutex names / Named pipes**
*   *(None identified in the provided text)*

**Hashes**
*   *(None identified in the provided string list)*

**Other artifacts**
*   **User-Agent:** `Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; CIBA; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022)`
*   **HTTP Headers:**
    *   `Accept: */*`
    *   `Content-Type: application/x-www-form-urlencoded`
    *   `Accept-Language: zh-cn`
    *   `Connection: Keep-Alive`
*   **Suspicious Keywords:** `microsofthelp`, `WindowsHookExON`

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: dropper/downloader
3. **Confidence**: High

4. **Key evidence**:
*   **Downloader Behavior:** The binary utilizes the `WinINET` library (`InternetReadFile`, `InternetOpenUrlA`) and manual memory management (`HeapAlloc`, `VirtualAlloc`) to fetch and stage secondary payloads from a remote server into memory.
*   **Evasion & Persistence:** The sample employs multiple anti-analysis techniques, including `Sleep()` loops to bypass sandboxes, dynamic API resolution to hide its import table, and the creation of a "Run" key for persistence.
*   **Masquerading Tactics:** Use of deceptive filenames like `microsofthelp.exe` and the inclusion of unconventional registry keys (e.g., `Software\motherFucker`) indicate intentional malicious intent and an attempt to blend in with system processes.
