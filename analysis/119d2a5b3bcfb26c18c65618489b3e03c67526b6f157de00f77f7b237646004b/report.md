# Threat Analysis Report

**Generated:** 2026-08-23 20:18 UTC
**Sample:** `119d2a5b3bcfb26c18c65618489b3e03c67526b6f157de00f77f7b237646004b_119d2a5b3bcfb26c18c65618489b3e03c67526b6f157de00f77f7b237646004b.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `119d2a5b3bcfb26c18c65618489b3e03c67526b6f157de00f77f7b237646004b_119d2a5b3bcfb26c18c65618489b3e03c67526b6f157de00f77f7b237646004b.exe` |
| File type | PE32 executable for MS Windows 5.00 (GUI), Intel i386, 5 sections |
| Size | 114,176 bytes |
| MD5 | `f3c7647e32dc50706c17b67379223c08` |
| SHA1 | `759a3164ef3d7a66ac35ee6b695cf9bc8fd7e2bc` |
| SHA256 | `119d2a5b3bcfb26c18c65618489b3e03c67526b6f157de00f77f7b237646004b` |
| Overall entropy | 6.361 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1773845403 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 80,384 | 6.55 | No |
| `.rdata` | 19,456 | 5.148 | No |
| `.data` | 5,120 | 3.027 | No |
| `.rsrc` | 512 | 5.105 | No |
| `.reloc` | 7,680 | 4.749 | No |

### Imports

**WININET.dll**: `InternetOpenA`, `InternetOpenUrlA`, `InternetOpenW`, `InternetOpenUrlW`, `InternetReadFile`, `InternetCloseHandle`
**SHLWAPI.dll**: `PathFileExistsW`
**KERNEL32.dll**: `SetStdHandle`, `WriteConsoleW`, `GetConsoleOutputCP`, `WriteConsoleA`, `LoadLibraryA`, `InitializeCriticalSectionAndSpinCount`, `Sleep`, `CreateProcessW`, `CloseHandle`, `CreateFileW`, `ExpandEnvironmentStringsW`, `GetLocaleInfoW`, `DeleteFileW`, `WriteFile`, `GetTickCount`
**USER32.dll**: `wsprintfW`
**SHELL32.dll**: `ShellExecuteW`

## Extracted Strings

Total strings found: **564** (showing first 100)

```
!This program cannot be run in DOS mode.
$
2Yc<v8ov8ov8o
vog8ov8o
ow8oRichv8o
`.rdata
@.data
@.reloc
thh4YA
tNh8YA
t4h<YA
tBhxYA
tHh`YA
FYY;uu
FYY;uu
t}9>uyj
M9^Lth
t_9]u
F 98u
F09^(u
8]t	V
u.j^9
QQSVWd
0WWWWW
AAFFf;
p;qt~
0WWWWW
0WWWWW
j
YQPVh
D$+d$SVW
D$+d$SVW
D$+d$SVW
F@uwV
F@uwV
F@WuyV
9}t$9}
9ut)9u
s[S;7|G;w
tR99u2
t"SS9]
u,9Et'9
tSSSSS
tSSSSS
tSSSSS
tVVVVV
tVVVVV
tVVVVV
t hx[A
E9Xt
tVVVVV
tVVVVV
tVVVVV
F\= kA
0A@@Ju
0SSSSS
>=Yt1j
QQSVWh
j@j ^V
t)jXP
t+WWVPV
tSSSSS
C PjPV
C$PjQV
C*PjTV
C+PjUV
C,PjVV
C-PjWV
C.PjRV
C/PjSV
0SSSSS
PPPPPPPP
0SSSSS
@9]|FVW
Y;Fu!
G9^t;
Y;Fu.j
u49^t/
PPPPPPPP
URPQQh
;t$,v-
kUQPXY]Y[
8
u
AA
VW|[;
u,VVWV
t VV9u
^SSSSS
^SSSSS
v	N+D$
<xt<Xt	
bad allocation
Tunnel
Tunnel
RtlGetVersion
http://178.16.54.109/lkdomain.exe
slack.exe
Teams.exe
Zoom.exe
sapgui.exe
PBIDesktop.exe
tableau.exe
http://158.94.211.162/1.exe
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00404f8a` | `0x404f8a` | 16863 | ✓ |
| `fcn.00406211` | `0x406211` | 5632 | ✓ |
| `fcn.0040cfd9` | `0x40cfd9` | 5334 | ✓ |
| `fcn.00403b86` | `0x403b86` | 5178 | ✓ |
| `fcn.0040eecc` | `0x40eecc` | 1843 | ✓ |
| `fcn.00412b3b` | `0x412b3b` | 1474 | ✓ |
| `fcn.00410f43` | `0x410f43` | 1051 | ✓ |
| `fcn.00409ba6` | `0x409ba6` | 933 | ✓ |
| `main` | `0x4016a0` | 879 | ✓ |
| `fcn.0040a530` | `0x40a530` | 869 | ✓ |
| `fcn.0040def0` | `0x40def0` | 869 | ✓ |
| `fcn.0040f7ed` | `0x40f7ed` | 844 | ✓ |
| `fcn.0040973c` | `0x40973c` | 839 | ✓ |
| `fcn.0040bcd4` | `0x40bcd4` | 790 | ✓ |
| `fcn.0040b3ad` | `0x40b3ad` | 770 | ✓ |
| `fcn.0040c483` | `0x40c483` | 741 | ✓ |
| `fcn.0040c1a2` | `0x40c1a2` | 737 | ✓ |
| `fcn.00403000` | `0x403000` | 690 | ✓ |
| `fcn.0040e786` | `0x40e786` | 596 | ✓ |
| `fcn.0040b17c` | `0x40b17c` | 561 | ✓ |
| `fcn.00413ea0` | `0x413ea0` | 559 | ✓ |
| `fcn.00410b16` | `0x410b16` | 539 | ✓ |
| `fcn.0040b6af` | `0x40b6af` | 539 | ✓ |
| `fcn.00412206` | `0x412206` | 497 | ✓ |
| `fcn.0040da27` | `0x40da27` | 485 | ✓ |
| `fcn.00401150` | `0x401150` | 484 | ✓ |
| `fcn.00401380` | `0x401380` | 447 | ✓ |
| `fcn.00410504` | `0x410504` | 442 | ✓ |
| `fcn.00410262` | `0x410262` | 436 | ✓ |
| `fcn.00410d93` | `0x410d93` | 432 | ✓ |

### Decompiled Code Files

- [`code/fcn.00401150.c`](code/fcn.00401150.c)
- [`code/fcn.00401380.c`](code/fcn.00401380.c)
- [`code/fcn.00403000.c`](code/fcn.00403000.c)
- [`code/fcn.00403b86.c`](code/fcn.00403b86.c)
- [`code/fcn.00404f8a.c`](code/fcn.00404f8a.c)
- [`code/fcn.00406211.c`](code/fcn.00406211.c)
- [`code/fcn.0040973c.c`](code/fcn.0040973c.c)
- [`code/fcn.00409ba6.c`](code/fcn.00409ba6.c)
- [`code/fcn.0040a530.c`](code/fcn.0040a530.c)
- [`code/fcn.0040b17c.c`](code/fcn.0040b17c.c)
- [`code/fcn.0040b3ad.c`](code/fcn.0040b3ad.c)
- [`code/fcn.0040b6af.c`](code/fcn.0040b6af.c)
- [`code/fcn.0040bcd4.c`](code/fcn.0040bcd4.c)
- [`code/fcn.0040c1a2.c`](code/fcn.0040c1a2.c)
- [`code/fcn.0040c483.c`](code/fcn.0040c483.c)
- [`code/fcn.0040cfd9.c`](code/fcn.0040cfd9.c)
- [`code/fcn.0040da27.c`](code/fcn.0040da27.c)
- [`code/fcn.0040def0.c`](code/fcn.0040def0.c)
- [`code/fcn.0040e786.c`](code/fcn.0040e786.c)
- [`code/fcn.0040eecc.c`](code/fcn.0040eecc.c)
- [`code/fcn.0040f7ed.c`](code/fcn.0040f7ed.c)
- [`code/fcn.00410262.c`](code/fcn.00410262.c)
- [`code/fcn.00410504.c`](code/fcn.00410504.c)
- [`code/fcn.00410b16.c`](code/fcn.00410b16.c)
- [`code/fcn.00410d93.c`](code/fcn.00410d93.c)
- [`code/fcn.00410f43.c`](code/fcn.00410f43.c)
- [`code/fcn.00412206.c`](code/fcn.00412206.c)
- [`code/fcn.00412b3b.c`](code/fcn.00412b3b.c)
- [`code/fcn.00413ea0.c`](code/fcn.00413ea0.c)
- [`code/main.c`](code/main.c)

## Behavioral Analysis

The additional disassembly provides significant technical detail regarding how the malware handles network communication, file system interaction, and environmental profiling. 

Here is the updated analysis, incorporating both sets of findings:

### Updated Analysis Report

#### **1. Core Functionality and Purpose**
The binary is a sophisticated **Downloader / Dropper**. It is designed to establish a connection with remote servers (C2 infrastructure) to download and execute additional payloads. The disassembly confirms that the malware does not just "fetch" data; it actively manages the persistence of those files on the disk by hiding their origin.

#### **.New Findings from Chunk 2:**

*   **Automated Payload Dropping & File System Manipulation:**
    In `fcn.00411500`, a clear dropper routine is identified:
    *   **Environment Variable Usage:** It uses `ExpandEnvironmentStringsW` to resolve the `%temp%` directory, a common staging area for malware because it often has relaxed permissions.
    *   **Dynamic Naming:** It uses a calculation (e.g., `iVar1 % 0x7fff + 1000`) to generate what appears to be a semi-randomized filename or ID for the downloaded `.exe`. This helps avoid detection by security tools looking for consistent, hardcoded filenames.
    *   **Zone Identifier Removal:** A key piece of evidence is found in the logic that targets files with the suffix `.Zone.Identifier`. By deleting this file after a download, the malware **strips the "Mark of the Web" (MOTW)**—a security feature in Windows that warns users when a file was downloaded from an untrusted source via a browser.

*   **Advanced Locale & Geofencing Logic:**
    Functions like `fcn.00412206` and `fcn.00410504` heavily utilize:
    *   `GetUserDefaultLCID`, `GetSystemDefaultLCID`, and `GetLocaleInfoA`.
    *   These calls are used to identify the victim's system language and region. This confirms the hypothesis that the malware is "geo-fenced" or tailored specifically for certain regions (e.g., specific countries or corporate hubs).

*   **Sophisticated Network Communication:**
    The code uses both `InternetOpenW` (Unicode) and `InternetOpenA` (ANSI), ensuring compatibility across different Windows configurations. 
    *   **User-Agent Masquerading:** The malware utilizes a hardcoded User-Agent string mimicking a standard Chrome browser on Windows 10: `Mozilla/5.0 (Windows NT 10.0; Win64; x64) ... Chrome/7775543322.0.0.0`. This is intended to blend in with legitimate web traffic during the download process.

*   **Internal Logic & Configuration Handling:**
    The functions `fcn.0040c483` and `fcn.0040b3ad` indicate a complex internal "engine." The malware seems to navigate a series of memory structures (likely a configuration table) to decide which actions to perform next, checking for system capabilities or specific environmental conditions before moving to the next stage.

---

### Consolidated Summary of Malicious Behaviors

| Category | Identified Behavior | Technical Detail / Evidence |
| :--- | :--- | :--- |
| **C2 Infrastructure** | Hardcoded IP/URL list | [178.16.54.109] and [158.94.211.162] for various `.exe` payloads. |
| **Staged Delivery** | Multi-stage Dropper | Uses a configuration table to decide which payload (e.g., `1.exe`–`13.exe`) to fetch based on the environment. |
| **Evasion Tech** | Anti-Forensics | **Deletes `.Zone.Identifier` files** to hide that a file was downloaded from the internet. |
| **Evasion Tech** | Sandboxing/Analysis | Includes `Sleep(2000)` at startup and uses complex string conversion wrappers to obfuscate data paths. |
| **Target Profiling** | Corporate Discovery | Searches for `slack.exe`, `Teams.exe`, `Zoom.exe`, and `sapgui.exe`. |
| **Geofencing** | Locale Detection | Uses `GetLocaleInfoA` and `GetUserDefaultLCID` to determine the user's location/language before proceeding. |
| **Stealth Tactics** | Browser Masquerading | Mimics a standard Chrome User-Agent during HTTP requests via WinINet APIs. |

### Conclusion
This is a high-quality piece of malware designed for **Initial Access**. It is not a simple "plug-and-play" downloader; it is highly modular and defensive. Its primary goal is to verify that the target is a valuable corporate machine (via Slack/Teams checks) and located in a specific region (via Locale checks) before downloading specialized tools or secondary malware payloads into the `%temp%` folder while actively removing forensic evidence of its source.

---

## MITRE ATT&CK Mapping

Based on the behavior analysis provided, here is the mapping to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1568.002** | Masquerading: User-Agent | The malware uses a hardcoded Chrome string to hide its identity and blend in with legitimate web traffic during downloads. |
| **T1070.004** | Indicator Removal on Host | By deleting `.Zone.Identifier` files, the malware removes "Mark of the Web" evidence to mask the file's origin from forensic tools. |
| **T1497** | Virtualization/Sandbox Detection | Locale and language checks are used as a filtering mechanism to ensure the payload only executes on systems in specific targeted regions. |
| **T1036** | Masquerading | The use of dynamic naming for downloaded files helps bypass security tools that look for consistent, hardcoded filenames. |
| **T1105** | Ingress Tool Transfer | The malware functions as a multi-stage downloader to fetch various payloads from remote infrastructure based on internal logic. |
| **T1083** | File and Directory Discovery | The search for applications like `slack.exe` and `Teams.exe` is used to identify high-value targets within a corporate environment. |
| **T1214** | Exploitation of Remote Services (Internal) | *Note: While not explicitly an exploit, the use of hardcoded IP/URLs for specific .exe payloads highlights the C2 infrastructure.* |

***

**Analyst Notes:**
*   The behavior identified in the report suggests a highly targeted **Initial Access** and **Execution** phase. 
*   The presence of both "Geofencing" (T1497) and "Corporate Discovery" (T1083) indicates that the threat actor is likely targeting specific organizations rather than performing broad, indiscriminate scanning.
*   The removal of Mark of the Web identifiers (T1070.004) specifically points to an intent to bypass security analyst scrutiny during post-incident forensics.

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

### **IP addresses / URLs / Domains**
*   **178.16.54.109** (C2 Infrastructure)
*   **158.94.211.162** (C2 Infrastructure)
*   **http://178.16.54.109/lkdomain.exe** (Payload Delivery URL)
*   **http://158.94.211.162/[1-14].exe** (Sequential Payload Download URLs)
*   **http://ip-api.com/json/** (Geolocation Check API)

### **File paths / Registry keys**
*   **%temp%** (Used as the primary staging directory for payloads)
*   **.Zone.Identifier** (Targeted for deletion to remove "Mark of the Web" metadata)
*   **lkdomain.exe** (Malicious payload filename)
*   **1.exe, 2.exe, ... 14.exe** (Numbered filenames used for staged delivery)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None found in provided strings.*

### **Other artifacts**
*   **User-Agent:** `Mozilla/5.0 (Windows NT 10.0; Win64; x64) ... Chrome/7775543322.0.0.0` (Used for browser masquerading)
*   **Targeted Corporate Applications (Profiling):**
    *   `slack.exe`
    *   `Teams.exe`
    *   `Zoom.exe`
    *   `sapgui.exe`
    *   `PBIDesktop.exe`
    *   `tableau.exe`
*   **C2 Pattern:** The use of an IP (158.94.211.162) hosting a sequence of numbered executables (`1.exe` through `14.exe`) indicates a multi-stage dropper logic where the specific payload is chosen based on environment checks.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://158.94.211.162/1.exe`
- `http://158.94.211.162/10.exe`
- `http://158.94.211.162/11.exe`
- `http://158.94.211.162/12.exe`
- `http://158.94.211.162/13.exe`
- `http://158.94.211.162/14.exe`
- `http://158.94.211.162/2.exe`
- `http://158.94.211.162/3.exe`
- `http://158.94.211.162/4.exe`
- `http://158.94.211.162/5.exe`
- `http://158.94.211.162/6.exe`
- `http://158.94.211.162/7.exe`
- `http://158.94.211.162/8.exe`
- `http://158.94.211.162/9.exe`
- `http://178.16.54.109/lkdomain.exe`
- `http://ip-api.com/json/`

**IP addresses:**
- `158.94.211.162`
- `178.16.54.109`

---

## Malware Family Classification

Based on the analysis provided, here is the classification of the sample:

1.  **Malware family:** custom
2.  **Malware type:** loader / dropper
3.  **Confidence:** High
4.  **Key evidence:**
    *   **Sophisticated Initial Access Tactics:** The malware performs advanced "corporate discovery" by searching for high-value targets (Slack, Teams, SAP GUI) and employs geofencing/locale checks to ensure it only executes on specific targeted environments.
    *   **Advanced Evasion & Anti-Forensics:** It actively hides its tracks by deleting `.Zone.Identifier` files (removing "Mark of the Web" labels) and uses a tailored Chrome User-Agent string to blend in with legitimate web traffic during its download phases.
    *   **Modular Multi-stage Delivery:** The use of a configuration table to select from 14 different possible executables based on environmental checks indicates a highly organized, modular architecture typical of advanced loaders designed to deliver secondary payloads (such as RATs or info-stealers).
