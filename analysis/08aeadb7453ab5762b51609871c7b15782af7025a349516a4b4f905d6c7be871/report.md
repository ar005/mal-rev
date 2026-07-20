# Threat Analysis Report

**Generated:** 2026-07-18 18:02 UTC
**Sample:** `08aeadb7453ab5762b51609871c7b15782af7025a349516a4b4f905d6c7be871_08aeadb7453ab5762b51609871c7b15782af7025a349516a4b4f905d6c7be871.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `08aeadb7453ab5762b51609871c7b15782af7025a349516a4b4f905d6c7be871_08aeadb7453ab5762b51609871c7b15782af7025a349516a4b4f905d6c7be871.exe` |
| File type | PE32 executable for MS Windows 5.00 (GUI), Intel i386, 5 sections |
| Size | 115,712 bytes |
| MD5 | `c1c333e46b57b2c12a96915e43b2939e` |
| SHA1 | `8aaba18e69dbfbce2515422f3306678fc491fd0d` |
| SHA256 | `08aeadb7453ab5762b51609871c7b15782af7025a349516a4b4f905d6c7be871` |
| Overall entropy | 6.356 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1769149119 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 80,384 | 6.557 | No |
| `.rdata` | 20,480 | 5.183 | No |
| `.data` | 5,632 | 2.917 | No |
| `.rsrc` | 512 | 5.105 | No |
| `.reloc` | 7,680 | 4.798 | No |

### Imports

**WININET.dll**: `InternetOpenA`, `InternetOpenUrlA`, `InternetOpenW`, `InternetOpenUrlW`, `InternetReadFile`, `InternetCloseHandle`
**SHLWAPI.dll**: `PathFileExistsW`
**KERNEL32.dll**: `SetStdHandle`, `WriteConsoleW`, `GetConsoleOutputCP`, `WriteConsoleA`, `LoadLibraryA`, `InitializeCriticalSectionAndSpinCount`, `Sleep`, `CreateProcessW`, `CloseHandle`, `CreateFileW`, `ExpandEnvironmentStringsW`, `GetLocaleInfoW`, `DeleteFileW`, `WriteFile`, `GetTickCount`
**USER32.dll**: `wsprintfW`
**SHELL32.dll**: `ShellExecuteW`

## Extracted Strings

Total strings found: **586** (showing first 100)

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
uh%S@
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
uQh|^A
tVVVVV
tVVVVV
tVVVVV
E9Xt
tVVVVV
tVVVVV
tVVVVV
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
Vj@h8uA
PPPPPPPP
URPQQh &A
;t$,v-
kUQPXY]Y[
8
u
AA
VW|[;0
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
http://195.178.136.19/1.exe
http://195.178.136.19/2.exe
http://195.178.136.19/3.exe
http://195.178.136.19/4.exe
http://195.178.136.19/5.exe
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00404faa` | `0x404faa` | 16863 | ✓ |
| `fcn.00406231` | `0x406231` | 5632 | ✓ |
| `fcn.0040cff9` | `0x40cff9` | 5334 | ✓ |
| `fcn.00403ba6` | `0x403ba6` | 5178 | ✓ |
| `fcn.0040eeec` | `0x40eeec` | 1843 | ✓ |
| `fcn.00412b5b` | `0x412b5b` | 1474 | ✓ |
| `fcn.00410f63` | `0x410f63` | 1051 | ✓ |
| `fcn.00409bc6` | `0x409bc6` | 933 | ✓ |
| `main` | `0x4016a0` | 909 | ✓ |
| `fcn.0040a550` | `0x40a550` | 869 | ✓ |
| `fcn.0040df10` | `0x40df10` | 869 | ✓ |
| `fcn.0040f80d` | `0x40f80d` | 844 | ✓ |
| `fcn.0040975c` | `0x40975c` | 839 | ✓ |
| `fcn.0040bcf4` | `0x40bcf4` | 790 | ✓ |
| `fcn.0040b3cd` | `0x40b3cd` | 770 | ✓ |
| `fcn.0040c4a3` | `0x40c4a3` | 741 | ✓ |
| `fcn.0040c1c2` | `0x40c1c2` | 737 | ✓ |
| `fcn.00403020` | `0x403020` | 690 | ✓ |
| `fcn.0040e7a6` | `0x40e7a6` | 596 | ✓ |
| `fcn.0040b19c` | `0x40b19c` | 561 | ✓ |
| `fcn.00413ec0` | `0x413ec0` | 559 | ✓ |
| `fcn.00410b36` | `0x410b36` | 539 | ✓ |
| `fcn.0040b6cf` | `0x40b6cf` | 539 | ✓ |
| `fcn.00412226` | `0x412226` | 497 | ✓ |
| `fcn.0040da47` | `0x40da47` | 485 | ✓ |
| `fcn.00401150` | `0x401150` | 484 | ✓ |
| `fcn.00401380` | `0x401380` | 447 | ✓ |
| `fcn.00410524` | `0x410524` | 442 | ✓ |
| `fcn.00410282` | `0x410282` | 436 | ✓ |
| `fcn.00410db3` | `0x410db3` | 432 | ✓ |

### Decompiled Code Files

- [`code/fcn.00401150.c`](code/fcn.00401150.c)
- [`code/fcn.00401380.c`](code/fcn.00401380.c)
- [`code/fcn.00403020.c`](code/fcn.00403020.c)
- [`code/fcn.00403ba6.c`](code/fcn.00403ba6.c)
- [`code/fcn.00404faa.c`](code/fcn.00404faa.c)
- [`code/fcn.00406231.c`](code/fcn.00406231.c)
- [`code/fcn.0040975c.c`](code/fcn.0040975c.c)
- [`code/fcn.00409bc6.c`](code/fcn.00409bc6.c)
- [`code/fcn.0040a550.c`](code/fcn.0040a550.c)
- [`code/fcn.0040b19c.c`](code/fcn.0040b19c.c)
- [`code/fcn.0040b3cd.c`](code/fcn.0040b3cd.c)
- [`code/fcn.0040b6cf.c`](code/fcn.0040b6cf.c)
- [`code/fcn.0040bcf4.c`](code/fcn.0040bcf4.c)
- [`code/fcn.0040c1c2.c`](code/fcn.0040c1c2.c)
- [`code/fcn.0040c4a3.c`](code/fcn.0040c4a3.c)
- [`code/fcn.0040cff9.c`](code/fcn.0040cff9.c)
- [`code/fcn.0040da47.c`](code/fcn.0040da47.c)
- [`code/fcn.0040df10.c`](code/fcn.0040df10.c)
- [`code/fcn.0040e7a6.c`](code/fcn.0040e7a6.c)
- [`code/fcn.0040eeec.c`](code/fcn.0040eeec.c)
- [`code/fcn.0040f80d.c`](code/fcn.0040f80d.c)
- [`code/fcn.00410282.c`](code/fcn.00410282.c)
- [`code/fcn.00410524.c`](code/fcn.00410524.c)
- [`code/fcn.00410b36.c`](code/fcn.00410b36.c)
- [`code/fcn.00410db3.c`](code/fcn.00410db3.c)
- [`code/fcn.00410f63.c`](code/fcn.00410f63.c)
- [`code/fcn.00412226.c`](code/fcn.00412226.c)
- [`code/fcn.00412b5b.c`](code/fcn.00412b5b.c)
- [`code/fcn.00413ec0.c`](code/fcn.00413ec0.c)
- [`code/main.c`](code/main.c)

## Behavioral Analysis

This updated analysis incorporates the findings from chunk 2/2. The additional disassembly confirms several high-risk behaviors, specifically regarding how the malware handles and prepares its secondary payloads.

### Updated Summary of Findings
The binary is confirmed as a **sophisticated downloader and "loader"** designed for use in multi-stage attacks. It doesn't just download files; it actively manages the environment to ensure those files are executed without triggering system warnings, while handling complex localized strings to maintain functionality across different geographical regions.

---

### New & Refined Suspicious Behaviors

#### 1. Anti-Forensics and Execution Optimization
A critical piece of logic was identified in `fcn.0041150`:
*   **Zone Identifier Removal:** After downloading an executable to the `%temp%` directory, the binary calls `DeleteFileW` on a file named `[path]:Zone.Identifier`. 
    *   **Significance:** This is a known technique used to strip the "Mark of the Web" (MotW) from files downloaded via a browser or network client. Removing this identifier prevents Windows from displaying security warnings when the user attempts to run the downloaded file, making the infection process much smoother and less suspicious to the end-user.
*   **Temp Directory Execution:** The use of `ExpandEnvironmentStringsW` to resolve `%temp%` followed by `wsprintfW` confirms that the malware intends to "drop" its next stage in a common temporary directory for execution.

#### 2. Robust Network Communication (WinINet API)
Multiple functions (`fcn.0041150` and `fcn.0041380`) utilize the Windows `WinINet` library:
*   **Standard Header Spoofing:** It uses a hardcoded User-Agent string (`Mozilla/5.0 ... Chrome/7775543322...`) to masquerade as a standard web browser when reaching out to Command & Control (C2) servers.
*   **Streamed Downloads:** The use of `InternetReadFile` in a loop indicates the malware is designed to handle large files by streaming them into memory/disk, which can sometimes bypass basic packet-inspection tools that only look for single, large file transfers.

#### 3. Internationalization and Localization Handling
The presence of several complex functions related to Unicode/MultiByte conversion (`fcn.00413ec0`, `fcn.0040da47`) suggests:
*   **Widespread Targeting:** The malware is designed to operate across different locales (e.g., it contains logic to handle specific code pages like `0x814` for Japanese). 
*   **Robustness:** It ensures that system paths, filenames, and environment variables are handled correctly regardless of the victim's language settings, ensuring it remains functional across a global target base.

---

### Technical Analysis of Internals
*   **Heap Management & Memory Manipulation:** Function `fcn.0040bcf4` indicates sophisticated memory management. The binary likely performs its own heap management to handle data buffers (like downloaded payloads) efficiently and perhaps to minimize the footprint left in standard system memory allocations.
*   **Dynamic Logic Paths:** The logic in `fcn.0040975c` and `fcn.00410b36` suggests a highly modular structure. The malware uses internal "check-lists" (as noted in the previous analysis) but adds complex state management to decide exactly which communication routine or decoding method to use based on variables it gathers during execution.

---

### Updated Summary for Incident Response

**Threat Profile:** High-Confidence Malicious Downloader / Stage-1 Dropper
**Key Indicators of Compromise (IoCs) & Tactics:**

1.  **Advanced Evasion:** The binary explicitly removes **Zone Identifiers**. This is a high-fidelity indicator of intent to bypass security "warnings" for and facilitate the execution of downstream payloads.
2.  **Automated Payload Staging:** It utilizes `%temp%` as a staging area, automatically naming files (e.g., `1.exe`, `2.exe`) based on a sequence or specific logic.
3.  **Sophisticated Networking:** The use of WinINet with spoofed User-Agents indicates a need to blend in with legitimate web traffic. 
4.  **Infrastructure:** Confirm the IP addresses and URLs found in Chunk 1 as active C2 infrastructure for delivering additional payloads (potential ransomware, info-stealers, or remote access trojans).

**Recommended Actions:**
*   **Block Known IPs/Domains:** Immediately block `178.16.54.109`, `195.178.136.19`, and the `ip-api.com` site used for geolocation checks.
*   **Hunt for Staged Files:** Scan systems for files matching the pattern `[number].exe` in `%TEMP%` or `%APPDATA%`.
*   **Identify Persistence:** Since this is a "downloader," look for evidence of secondary payloads that may have been dropped after the initial infection (e.g., scheduled tasks, registry run keys). 
*   **Monitor Network Traffic:** Look for connections to WinINet-based requests using the "Mozilla/5.0" string toward the identified C2 IPs.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1562.001** | Data Manipulation Implicitly Filtering for Privilege Escalation | The malware deletes `Zone.Identifier` files to remove "Mark of the Web" indicators and bypass security warnings. |
| **T1036** | Masquerading | The malware uses a hardcoded, standard "Mozilla/5.0" User-Agent string to blend in with legitimate web traffic. |
| **T1105** | Ingress Tool Transfer | The malware utilizes the WinINet library and `InternetReadFile` to fetch and stream additional payloads from remote infrastructure. |
| **T1204.001** | Exploitation for Privilege Escalation (via staged files) | The use of `%temp%` as a staging area for sequentially named executables (`1.exe`, `2.exe`) facilitates automated multi-stage execution. |
| **T1027** | Obfuscated Files or Information | The complex "check-lists" and dynamic logic paths are used to manage state and choose execution paths, potentially to evade signature-based detection. |

***Note on Analysis:** While several behaviors (like high memory management efficiency and localization) indicate a sophisticated development cycle, they primarily support the classification of the malware as a **Loader/Downloader** rather than representing individual unique ATT&CK techniques.*

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs) categorized by type:

**IP addresses / URLs / Domains**
*   **178.16.54.109** (IP address)
*   **http://178.16.54.109/lkdomain.exe** (URL)
*   **195.178.136.19** (IP address used for a sequence of staged payloads)
*   **ip-api.com** (Domain used for geolocation checks)

**File paths / Registry keys**
*   **%temp%** (Used as a staging directory for payload extraction)
*   **[number].exe** (e.g., `1.exe`, `2.exe` ... `40.exe` - Used as naming convention for staged payloads in the temp directory)

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   *None identified in provided strings.*

**Other artifacts**
*   **User-Agent:** `Mozilla/5.0 ... Chrome/7775543322...` (Used to masquerade as a standard web browser)
*   **Anti-Forensics Technique:** Removal of **Zone.Identifier** files (specifically `[path]:Zone.Identifier`) to bypass Mark of the Web (MotW) security warnings.
*   **C2 Pattern:** Sequential host file structure (e.g., `1.exe` through `40.exe`) hosted on a single IP to deliver multi-stage components.

---
**Analyst Note:** The malware demonstrates high-sophistication in its delivery chain, utilizing common system directories for staging and standard browser User-Agents to blend into network traffic. The most critical indicators for blocking are the two primary IP addresses (`178.16.54.109` and `195.178.136.19`).

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://178.16.54.109/lkdomain.exe`
- `http://195.178.136.19/1.exe`
- `http://195.178.136.19/10.exe`
- `http://195.178.136.19/11.exe`
- `http://195.178.136.19/12.exe`
- `http://195.178.136.19/13.exe`
- `http://195.178.136.19/14.exe`
- `http://195.178.136.19/15.exe`
- `http://195.178.136.19/16.exe`
- `http://195.178.136.19/17.exe`
- `http://195.178.136.19/18.exe`
- `http://195.178.136.19/19.exe`
- `http://195.178.136.19/2.exe`
- `http://195.178.136.19/20.exe`
- `http://195.178.136.19/21.exe`
- `http://195.178.136.19/22.exe`
- `http://195.178.136.19/23.exe`
- `http://195.178.136.19/24.exe`
- `http://195.178.136.19/25.exe`
- `http://195.178.136.19/26.exe`
- `http://195.178.136.19/27.exe`
- `http://195.178.136.19/28.exe`
- `http://195.178.136.19/29.exe`
- `http://195.178.136.19/3.exe`
- `http://195.178.136.19/30.exe`
- `http://195.178.136.19/31.exe`
- `http://195.178.136.19/33.exe`
- `http://195.178.136.19/34.exe`
- `http://195.178.136.19/35.exe`
- `http://195.178.136.19/36.exe`
- `http://195.178.136.19/37.exe`
- `http://195.178.136.19/38.exe`
- `http://195.178.136.19/39.exe`
- `http://195.178.136.19/4.exe`
- `http://195.178.136.19/40.exe`
- `http://195.178.136.19/5.exe`
- `http://195.178.136.19/6.exe`
- `http://195.178.136.19/7.exe`
- `http://195.178.136.19/8.exe`
- `http://195.178.136.19/9.exe`
- `http://ip-api.com/json/`

**IP addresses:**
- `178.16.54.109`
- `195.178.136.19`

---

## Malware Family Classification

1. **Malware family**: Unknown (Custom Loader)
2. **Malware type**: loader / dropper
3. **Confidence**: High

4. **Key evidence**:
*   **Multi-Stage Execution:** The binary is specifically designed to download and stage multiple subsequent payloads in the `%temp%` directory using a sequence naming convention (`1.exe`, `2.exe`), indicating its role as a primary entry point for further infection.
*   **Anti-Forensics & Evasion:** It actively performs "Mark of the Web" (MotW) stripping by deleting `.Zone.Identifier` files, a high-confidence indicator that the malware is designed to bypass Windows security warnings for downstream payloads.
*   **Sophisticated Networking:** The use of `WinINet` with hardcoded browser User-Agents and its ability to handle complex internationalization/localization indicates it is a professional-grade tool designed to facilitate broad, multi-regional infections.
