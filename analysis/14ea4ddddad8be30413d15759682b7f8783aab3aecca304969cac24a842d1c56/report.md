# Threat Analysis Report

**Generated:** 2026-09-06 12:35 UTC
**Sample:** `14ea4ddddad8be30413d15759682b7f8783aab3aecca304969cac24a842d1c56_14ea4ddddad8be30413d15759682b7f8783aab3aecca304969cac24a842d1c56.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `14ea4ddddad8be30413d15759682b7f8783aab3aecca304969cac24a842d1c56_14ea4ddddad8be30413d15759682b7f8783aab3aecca304969cac24a842d1c56.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386 (stripped to external PDB), 3 sections |
| Size | 129,546 bytes |
| MD5 | `d2919781f5b3bc6700eb5c9900d5ac63` |
| SHA1 | `86a90f4e787f57a669674a9b4fd3dcdd5542b955` |
| SHA256 | `14ea4ddddad8be30413d15759682b7f8783aab3aecca304969cac24a842d1c56` |
| Overall entropy | 3.091 |
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

Total strings found: **531** (showing first 100)

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

This analysis details the functionality of the provided binary sample based on the decompiled code and associated strings.

### Core Functionality and Purpose
The binary appears to be a **malicious loader or "dropper."** It is designed to establish a foothold on a system, download additional components from a remote server, and ensure its persistence across reboots. The presence of `WinINet` functions alongside dynamic API loading suggests it acts as a multi-stage downloader.

### Suspicious and Malicious Behaviors
*   **Network Communication & Data Retrieval:**
    *   The function `fcn.004017c0` utilizes the **WinINet** library (`InternetOpenA`, `InternetSetOptionExA`, `InternetOpenUrlA`, and `InternetReadFile`). 
    *   It is designed to connect to a remote URL, retrieve data (likely a secondary payload or configuration file), and store it in a heap-allocated buffer. This is a classic "Downloader" behavior.
*   **Persistence Mechanism:**
    *   The strings explicitly reference `Software\Microsoft\Windows\CurrentVersion\Run`. 
    *   The code includes logic to interact with the Registry (`RegOpenKeyExA`, `RegSetValueExA`). Creating or modifying a key in the "Run" folder ensures that the malware automatically executes every time the user logs into Windows.
*   **Dynamic API Loading (Evasion/Obfuscation):**
    *   Multiple functions (e.g., `fcn.00401510`, `fcn.00403615`) use `LoadLibraryA` and `GetProcAddress`. 
    *   Instead of calling "noisy" functions directly (which would be caught by basic static analysis), the binary resolves function addresses at runtime. This is often used to hide the actual intent of the code, such as hidden network capabilities or process injection routines.
*   **Self-Deletion/Cleanup:**
    *   The routine involving `fcn.00401c80` followed by `DeleteFileA` suggests a "cleaner" mechanism. After the initial payload is dropped and executed, the malware may attempt to delete its original dropper file from the disk to hide its tracks from forensic analysis.
*   **Environment/Information Gathering:**
    *   The presence of strings like `%s?mac=%02X-%02X...` suggests it gathers system information (like MAC addresses) for "fingerprinting" or identifying the specific victim machine before exfiltrating data or deciding which payload to deliver.

### Notable Techniques and Patterns
*   **Reflective/Dynamic Execution:** The heavy use of `GetProcAddress` combined with shellcode-like jumps in some areas suggests a modular design where different capabilities are loaded into memory only when needed.
*   **Resource Obfuscation:** The code contains several loops that process data to "de-obfuscate" values before using them as paths or configuration constants. 
*   **Telltale Signatures:**
    *   The Registry key `Software\motherFucker` is an explicit indicator of malicious intent (likely a naming convention used by the developer).
    *   The use of `Sleep()` calls between network operations or after certain tasks are completed is a common **anti-analysis** technique used to "outwait" automated sandboxes that only monitor for a short period.
*   **Heavy Windows API Utilization:** The usage of `WinINet`, `Advapi32` (Registry), and `Shell32` indicates a sophisticated ability to interact with the OS to achieve its goals of persistence and networking.

### Summary Table of Risks
| Category | Observation | Threat Level |
| :--- | :--- | :--- |
| **Persistence** | Registry "Run" key manipulation | High |
| **Networking** | `WinINet` based downloader component | High |
| **Evasion** | Dynamic API resolution (`GetProcAddress`) | Medium |
| **Stealth** | Self-deletion of components after execution | Medium |

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1105** | Ingress Tool Transfer | The binary uses the `WinINet` library to retrieve and store a remote payload into a heap-allocated buffer. |
| **T1547.001** | Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder | The binary modifies the `Software\Microsoft\Windows\CurrentVersion\Run` key to ensure execution upon user login. |
| **T1027** | Obfuscated Files or Information | The use of `LoadLibraryA` and `GetProcAddress` hides "noisy" API calls from static analysis tools. |
| **T1070.004** | Indicator Removal on Host: File Deletion | The binary includes a specific routine to delete its own components/dropper file after execution to evade forensic detection. |
| **T1082** | System Information Discovery | The code specifically gathers system metrics like MAC addresses to perform fingerprinting of the victim machine. |
| **T1497** | Virtualization/Sandbox Evasion | The implementation of `Sleep()` calls between network activities is used to bypass automated sandboxes with time-limited analysis. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the identified Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*(No specific IP addresses or hardcoded domains were identified in the provided text; however, the use of WinINet functions suggests a dynamically generated URL structure).*

**File paths / Registry keys**
*   `Software\motherFucker` (Highly suspicious registry key)
*   `\microsofthelp.exe` (Suspicious file name/path)
*   `HidePlugin.dll` (Potential malicious DLL component)
*   `Software\Microsoft\Windows\CurrentVersion\Run` (Persistence mechanism identified in behavior analysis)

**Mutex names / Named pipes**
*(None identified)*

**Hashes**
*(None found in the provided strings)*

**Other artifacts**
*   **User Agent:** `Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; CIBA; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022)`
*   **HTTP Headers:** 
    *   `Accept: */*`
    *   `Content-Type: application/x-www-form-urlencoded`
    *   `Accept-Language: zh-cn`
    *   `Connection: Keep-Alive`
*   **Behavioral Note:** The use of `GetProcAddress` and `LoadLibraryA` for dynamic API resolution is noted as a specific evasion technique.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader / dropper
3. **Confidence**: High

**Key evidence**:
*   **Multi-Stage Execution:** The use of `WinINet` to fetch and store remote payloads in heap-allocated buffers, along with the presence of a secondary component (`HidePlugin.dll`), confirms its primary role as a loader/dropper.
*   **Persistence & Stealth:** The binary implements standard "survival" tactics by creating a registry key for persistence (`Software\motherFucker`) and includes self-deletion routines to remove the initial dropper from the disk after execution.
*   **Evasion Tactics:** The heavy reliance on dynamic API resolution (`GetProcAddress`, `LoadLibraryA`), anti-analysis `Sleep()` calls, and MAC address fingerprinting are characteristic of a sophisticated first-stage loader designed to bypass automated sandboxes.
