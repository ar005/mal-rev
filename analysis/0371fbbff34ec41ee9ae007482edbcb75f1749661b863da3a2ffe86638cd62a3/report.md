# Threat Analysis Report

**Generated:** 2026-06-30 00:08 UTC
**Sample:** `0371fbbff34ec41ee9ae007482edbcb75f1749661b863da3a2ffe86638cd62a3_0371fbbff34ec41ee9ae007482edbcb75f1749661b863da3a2ffe86638cd62a3.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0371fbbff34ec41ee9ae007482edbcb75f1749661b863da3a2ffe86638cd62a3_0371fbbff34ec41ee9ae007482edbcb75f1749661b863da3a2ffe86638cd62a3.exe` |
| File type | PE32 executable for MS Windows 5.00 (GUI), Intel i386, 5 sections |
| Size | 113,152 bytes |
| MD5 | `5e93cfd01bac9ac4729f29be8f67de15` |
| SHA1 | `9c31065da22663f8060b87bc7f28f46d43a41148` |
| SHA256 | `0371fbbff34ec41ee9ae007482edbcb75f1749661b863da3a2ffe86638cd62a3` |
| Overall entropy | 6.367 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1780049401 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 79,872 | 6.549 | No |
| `.rdata` | 18,944 | 5.187 | No |
| `.data` | 5,120 | 3.015 | No |
| `.rsrc` | 512 | 5.105 | No |
| `.reloc` | 7,680 | 4.71 | No |

### Imports

**WININET.dll**: `InternetOpenA`, `InternetOpenUrlA`, `InternetOpenW`, `InternetOpenUrlW`, `InternetReadFile`, `InternetCloseHandle`
**SHLWAPI.dll**: `PathFileExistsW`
**KERNEL32.dll**: `SetStdHandle`, `WriteConsoleW`, `GetConsoleOutputCP`, `WriteConsoleA`, `LoadLibraryA`, `InitializeCriticalSectionAndSpinCount`, `Sleep`, `CreateProcessW`, `CloseHandle`, `CreateFileW`, `ExpandEnvironmentStringsW`, `GetLocaleInfoW`, `DeleteFileW`, `WriteFile`, `GetTickCount`
**USER32.dll**: `wsprintfW`
**SHELL32.dll**: `ShellExecuteW`

## Extracted Strings

Total strings found: **552** (showing first 100)

```
!This program cannot be run in DOS mode.
$
2Yc<v8ov8ov8o
vog8ov8o
ow8oRichv8o
`.rdata
@.data
@.reloc
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
uQhpZA
tVVVVV
tVVVVV
tVVVVV
E9Xt
tVVVVV
tVVVVV
tVVVVV
F\=pjA
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
Vj@h(qA
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
http://178.16.54.109/lb1.exe
http://178.16.54.109/lb2.exe
http://178.16.54.109/lb3.exe
http://178.16.54.109/lb4.exe
http://178.16.54.109/lb5.exe
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00404d4a` | `0x404d4a` | 16863 | ✓ |
| `fcn.00405fd1` | `0x405fd1` | 5632 | ✓ |
| `fcn.0040cd99` | `0x40cd99` | 5334 | ✓ |
| `fcn.00403946` | `0x403946` | 5178 | ✓ |
| `fcn.0040ec8c` | `0x40ec8c` | 1843 | ✓ |
| `fcn.004128fb` | `0x4128fb` | 1474 | ✓ |
| `fcn.00410d03` | `0x410d03` | 1051 | ✓ |
| `fcn.00409966` | `0x409966` | 933 | ✓ |
| `fcn.0040a2f0` | `0x40a2f0` | 869 | ✓ |
| `fcn.0040dcb0` | `0x40dcb0` | 869 | ✓ |
| `fcn.0040f5ad` | `0x40f5ad` | 844 | ✓ |
| `fcn.004094fc` | `0x4094fc` | 839 | ✓ |
| `fcn.0040ba94` | `0x40ba94` | 790 | ✓ |
| `fcn.0040b16d` | `0x40b16d` | 770 | ✓ |
| `fcn.0040c243` | `0x40c243` | 741 | ✓ |
| `fcn.0040bf62` | `0x40bf62` | 737 | ✓ |
| `fcn.00402dc0` | `0x402dc0` | 690 | ✓ |
| `fcn.0040e546` | `0x40e546` | 596 | ✓ |
| `fcn.0040af3c` | `0x40af3c` | 561 | ✓ |
| `fcn.00413c60` | `0x413c60` | 559 | ✓ |
| `fcn.004108d6` | `0x4108d6` | 539 | ✓ |
| `fcn.0040b46f` | `0x40b46f` | 539 | ✓ |
| `fcn.00411fc6` | `0x411fc6` | 497 | ✓ |
| `fcn.0040d7e7` | `0x40d7e7` | 485 | ✓ |
| `fcn.00401150` | `0x401150` | 484 | ✓ |
| `fcn.00401380` | `0x401380` | 447 | ✓ |
| `fcn.004102c4` | `0x4102c4` | 442 | ✓ |
| `fcn.00410023` | `0x410023` | 436 | ✓ |
| `fcn.00410b53` | `0x410b53` | 432 | ✓ |
| `method.std::basic_filebuf_char__struct_std::char_traits_char__.virtual_4` | `0x40440e` | 431 | ✓ |

### Decompiled Code Files

- [`code/fcn.00401150.c`](code/fcn.00401150.c)
- [`code/fcn.00401380.c`](code/fcn.00401380.c)
- [`code/fcn.00402dc0.c`](code/fcn.00402dc0.c)
- [`code/fcn.00403946.c`](code/fcn.00403946.c)
- [`code/fcn.00404d4a.c`](code/fcn.00404d4a.c)
- [`code/fcn.00405fd1.c`](code/fcn.00405fd1.c)
- [`code/fcn.004094fc.c`](code/fcn.004094fc.c)
- [`code/fcn.00409966.c`](code/fcn.00409966.c)
- [`code/fcn.0040a2f0.c`](code/fcn.0040a2f0.c)
- [`code/fcn.0040af3c.c`](code/fcn.0040af3c.c)
- [`code/fcn.0040b16d.c`](code/fcn.0040b16d.c)
- [`code/fcn.0040b46f.c`](code/fcn.0040b46f.c)
- [`code/fcn.0040ba94.c`](code/fcn.0040ba94.c)
- [`code/fcn.0040bf62.c`](code/fcn.0040bf62.c)
- [`code/fcn.0040c243.c`](code/fcn.0040c243.c)
- [`code/fcn.0040cd99.c`](code/fcn.0040cd99.c)
- [`code/fcn.0040d7e7.c`](code/fcn.0040d7e7.c)
- [`code/fcn.0040dcb0.c`](code/fcn.0040dcb0.c)
- [`code/fcn.0040e546.c`](code/fcn.0040e546.c)
- [`code/fcn.0040ec8c.c`](code/fcn.0040ec8c.c)
- [`code/fcn.0040f5ad.c`](code/fcn.0040f5ad.c)
- [`code/fcn.00410023.c`](code/fcn.00410023.c)
- [`code/fcn.004102c4.c`](code/fcn.004102c4.c)
- [`code/fcn.004108d6.c`](code/fcn.004108d6.c)
- [`code/fcn.00410b53.c`](code/fcn.00410b53.c)
- [`code/fcn.00410d03.c`](code/fcn.00410d03.c)
- [`code/fcn.00411fc6.c`](code/fcn.00411fc6.c)
- [`code/fcn.004128fb.c`](code/fcn.004128fb.c)
- [`code/fcn.00413c60.c`](code/fcn.00413c60.c)
- [`code/method.std__basic_filebuf_char__struct_std__char_traits_char__.virtual_4.c`](code/method.std__basic_filebuf_char__struct_std__char_traits_char__.virtual_4.c)

## Behavioral Analysis

Based on the analysis of the second chunk of disassembly, I have updated and expanded the profile of the malware. The new code reinforces the previous classification of a **Downloader/Dropper** while adding specific evidence of **Anti-Forensics**, **Evasion Techniques**, and **Multi-stage Execution**.

### Updated Summary of Analysis

The additional disassembly provides concrete evidence for the technical mechanisms the malware uses to execute its primary objectives. Specifically, it reveals how the malware handles downloads, hides its tracks from security software, and manages environment-specific configurations.

---

### New Findings & Enhanced Behaviors

#### 1. Advanced Evasion & Anti-Forensics
*   **Zone Identifier Deletion:** In `fcn.00401150`, the malware explicitly constructs a path to a file's `:Zone.Identifier` and calls `DeleteFileW`. This is a high-confidence indicator of anti-forensic behavior; by deleting this "Mark of the Web" (MOTW), the malware attempts to hide the fact that the file was downloaded from an untrusted source, bypassing security tools that flag such files.
*   **Browser Masquerading:** The code uses a hardcoded, realistic User-Agent string (`Mozilla/5.0 ... Chrome/7775543322...`) when initiating HTTP connections via `InternetOpenW`. This is intended to blend in with normal web traffic and bypass basic security filters that block non-browser requests.
*   **Randomized Filenaming:** In `fcn.00411910` (and related logic), the malware utilizes calculations based on `GetTickCount()` and modulo operations to generate numbers for filenames in the `%temp%` directory (e.g., `[num][num].exe`). This helps avoid detection by signature-based tools that look for static, predictable filenames like `lkdomain.exe`.

#### 2. Robust Downloader Infrastructure
*   **Dual Download Paths:** The presence of two distinct download functions (`fcn.00401150` and `fcn.00401380`) suggests a modular architecture. One function may be the primary downloader, while the other acts as a fallback or a way to fetch different components (e.g., one for information gathering tools, another for persistent backdoors).
*   **Standard Library Exploitation:** The extensive code related to locale handling (`GetSystemDefaultLCID`, `EnumSystemLocalesA`), character set conversions (`MultiByteToWideChar`, `WideCharToMultiByte`), and Unicode/ANSI management indicates a high level of professional coding. This ensures the malware is highly portable across different system locales, a common trait in sophisticated modern malware.

#### 3. Execution Flow & Payload Handling
*   **Data Buffer Processing:** The routine `fcn.004018a0` (called after `InternetReadFile`) suggests that once data is pulled from the network, it may be decrypted or processed in memory before being written to disk or executed. This "in-memory" processing helps bypass security scanners that only monitor files on the disk.
*   **Persistence Readiness:** The use of `%temp%` as a primary landing zone for downloaded executables is a standard tactic to ensure high permissions and commonality across various user profiles, facilitating easier movement within a local network if successful.

---

### Updated Summary of Findings

| Category | Specific Behavior | Evidence/Technique |
| :--- | :--- | :--- |
| **Primary Role** | **Multi-Stage Downloader** | Uses multiple functions to fetch remote components; utilizes high-level C++ wrappers to hide logic. |
| **Evasion** | **Anti-Forensics (MOTW)** | Explicitly deletes `:Zone.Identifier` from downloaded files. |
| **Evasion** | **Network Masquerading** | Hardcoded legitimate Chrome User-Agent strings for HTTP requests. |
| **Evasion** | **Dynamic Filenaming** | Uses math/system timers to generate random numbers for local filenames. |
| **Reconnaissance** | **Targeted Identification** | (From Chunk 1) Checks for corporate tools like Slack, Teams, and SAP. |
| **Infrastructure** | **Hardcoded C2** | Static IP and URLs for retrieving modules (`lkdomain.exe`, `lb1.exe`). |

### Conclusion of Analysis (Updated)
This sample is a highly competent **Initial Access Loader**. It is designed not just to download files, but to do so while actively stripping away digital fingerprints that would alert security professionals or automated systems. Its modularity suggests it acts as a "Swiss Army Knife" for an attacker: once the initial infection succeeds, it can be switched between different payloads (info-stealers, ransomware, etc.) based on whether it detects high-value targets like SAP or corporate communication tools.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the behaviors identified in your report to the corresponding MITRE ATT&CK techniques and sub-techniques below:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1070** | Indicator Removal on Host | The deletion of `:Zone.Identifier` files is a classic anti-forensic technique used to remove the "Mark of the Web" and hide the fact that a file was downloaded from an untrusted source. |
| **T1036** | Masquerading | Using a hardcoded, realistic Chrome User-Agent string allows the malware to blend in with legitimate web traffic to bypass security filters. |
| **T1036** | Masquerading | Generating randomized filenames using `GetTickCount()` avoids detection by signature-based security tools that look for static, predictable file names. |
| **T1105** | Ingress Tool Transfer | The multi-stage architecture and the use of distinct download functions indicate a downloader designed to retrieve additional components or modules from remote infrastructure. |
| **T1027** | Obfuscation | Processing data in memory (in-memory processing) before execution is used to bypass security scanners that only monitor files residing on the disk. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

### **IP addresses / URLs / Domains**
*   **178.16.54.109** (C2 IP Address)
*   **http://178.16.54.109/lkdomain.exe** (Payload Delivery URL)
*   **http://178.16.54.109/lb1.exe** through **http://178.16.54.109/lb10.exe** (Component Download URLs)
*   **http://ip-api.com/json/** (External API used for geolocation/IP info)

### **File paths / Registry keys**
*   **%temp%** (Used as a staging directory for dropped payloads)
*   **[FileName]:Zone.Identifier** (Targeted for deletion to remove "Mark of the Web" status)

### **Mutex names / Named pipes**
*   **MyAgent** (Potential internal identifier/mutex)

### **Hashes**
*   *None identified in provided text.*

### **Other artifacts**
*   **User-Agent:** `Mozilla/5.0 ... Chrome/7775543322...` (Hardcoded string used to masquerade as a standard browser)
*   **Malicious Filenames:** 
    *   `lkdomain.exe`
    *   `lb1.exe`, `lb2.exe`, `lb3.exe`, `lb4.exe`, `lb5.exe`, `lb6.exe`, `lb7.exe`, `lb8.exe`, `lb9.exe`, `lb10.exe`
*   **Targeted Environment Indicators (Corporate Software Checks):**
    *   The following strings indicate the malware checks for specific corporate software to determine the value of a target:
        *   `slack.exe`
        *   `Teams.exe`
        *   `Zoom.exe`
        *   `sapgui.exe`
        *   `PBIDesktop.exe`
        *   `tableau.exe`

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High

**Key evidence**:
*   **Anti-Forensic Evasion:** The sample actively deletes `:Zone.Identifier` metadata (Mark of the Web) and utilizes randomized filenames based on `GetTickCount()` to bypass security tools and hide its origin/presence.
*   **Multi-Stage Infrastructure:** It acts as a "Swiss Army Knife" loader, using multiple hardcoded C2 endpoints to fetch various modules (`lkdomain.exe`, `lb1...10.exe`) designed for different payloads or functionalities.
*   **Targeted Profiling:** The inclusion of specific checks for corporate software (SAP, Slack, Teams, Zoom) indicates a sophisticated design intended to identify high-value targets within a corporate environment before deploying further components.
