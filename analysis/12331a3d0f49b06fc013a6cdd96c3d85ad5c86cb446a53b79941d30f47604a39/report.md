# Threat Analysis Report

**Generated:** 2026-08-25 00:49 UTC
**Sample:** `12331a3d0f49b06fc013a6cdd96c3d85ad5c86cb446a53b79941d30f47604a39_12331a3d0f49b06fc013a6cdd96c3d85ad5c86cb446a53b79941d30f47604a39.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `12331a3d0f49b06fc013a6cdd96c3d85ad5c86cb446a53b79941d30f47604a39_12331a3d0f49b06fc013a6cdd96c3d85ad5c86cb446a53b79941d30f47604a39.exe` |
| File type | PE32+ executable for MS Windows 5.02 (GUI), x86-64 (stripped to external PDB), 10 sections |
| Size | 187,904 bytes |
| MD5 | `8e7d282e1bc3ac2ec58b3764e4435e17` |
| SHA1 | `6825e9e483abe77a44680ee25590497db8d52baf` |
| SHA256 | `12331a3d0f49b06fc013a6cdd96c3d85ad5c86cb446a53b79941d30f47604a39` |
| Overall entropy | 6.1 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1769125854 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 128,000 | 6.061 | No |
| `.data` | 3,584 | 3.41 | No |
| `.rdata` | 42,496 | 4.977 | No |
| `.pdata` | 2,560 | 4.714 | No |
| `.xdata` | 3,072 | 4.605 | No |
| `.bss` | 0 | 0.0 | No |
| `.idata` | 4,608 | 4.365 | No |
| `.CRT` | 512 | 0.377 | No |
| `.tls` | 512 | -0.0 | No |
| `.reloc` | 1,536 | 4.393 | No |

### Imports

**ADVAPI32.dll**: `RegCloseKey`, `RegOpenKeyExW`, `RegQueryValueExW`
**KERNEL32.dll**: `CloseHandle`, `CopyFileW`, `CreateDirectoryW`, `CreateFileA`, `CreatePipe`, `CreateThread`, `DeleteCriticalSection`, `DeleteFileW`, `EnterCriticalSection`, `ExpandEnvironmentStringsW`, `FindClose`, `FindFirstFileW`, `FindNextFileW`, `GetComputerNameW`, `GetCurrentProcess`
**msvcrt.dll**: `___lc_codepage_func`, `___mb_cur_max_func`, `__getmainargs`, `__initenv`, `__iob_func`, `__lconv_init`, `__set_app_type`, `__setusermatherr`, `_acmdln`, `_amsg_exit`, `_cexit`, `_commode`, `_errno`, `_fmode`, `_initterm`
**USER32.dll**: `MessageBoxW`
**WS2_32.dll**: `WSAGetLastError`, `WSAStartup`, `__WSAFDIsSet`, `closesocket`, `connect`, `freeaddrinfo`, `getaddrinfo`, `gethostbyname`, `htons`, `inet_ntoa`, `ntohs`, `recv`, `select`, `send`, `setsockopt`

## Extracted Strings

Total strings found: **1008** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.data
.rdata
@.pdata
@.xdata
.idata
.reloc
AUATUWVSH
[^_]A\A]
[^_]A\A]
AVAUATWVSH
[^_A\A]A^
AUATUWVSH
[^_]A\A]
AWAVAUATUWVSH
D$H9D$Lu?
X[^_]A\A]A^A_
AWAVAUATUWVSH
[^_]A\A]A^A_
AWAVAUATSH
 [A\A]A^A_
AVAUATVSH
[^A\A]A^
2t19
u
AVAUATWVSH
([^_A\A]A^
([^_A\A]A^
AVAUATUWVS
[^_]A\A]A^A_
AWAVAUATUWVSH
<\t=<

[^_]A\A]A^A_
cust_3daH
6eb6184dH
AWAVAUATUWVSH
[^_]A\A]A^A_
AWAVAUATUWVSH
[^_]A\A]A^A_
AVAUATUWVS
[^_]A\A]A^A_
AVAUATUWVS
[^_]A\A]A^A_
AWAVAUATUWVSH
[^_]A\A]A^A_
T$<=@B
AUATWVSH
[^_A\A]
AUATWVSH
[^_A\A]
AWAVAUATUWVSH
[^_]A\A]A^A_
AVAUATSH
[A\A]A^
AUATSH
0[A\A]
ATWVSH
([^_A\
AVAUATUWVSH
0[^_]A\A]A^
AWAVAUATUWVSH
[^_]A\A]A^A_
LcD$hH
AWAVAUATUWVSH
X[^_]A\A]A^A_
AVAUATUWVS
[^_]A\A]A^A_
AWAVAUATUWVSH
[^_]A\A]A^A_
AUATUWVS
[^_]A\A]A^
AVAUATUWVS
cust_3daH
6eb6184dH
H;\$Pt
cust_3daH
6eb6184dH
AVAUATUWVSH
[^_]A\A]A^
AWAVAUATUWVSH
[^_]A\A]A^A_
AWAVAUATUWVSH
========L
======
 H
      INH
========H
 LIST   H
    
===L
STALLED H
PROGRAMSf
[^_]A\A]A^A_
AWAVAUATUWVSH
[^_]A\A]A^A_
[^_]A\A]A^A_
AWAVAUATUWVSH
========A
========H
======
 H
      RUH
NNING PRH
OCESSES H
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **6**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.1400202c0` | `0x1400202c0` | 46258 | ✓ |
| `fcn.140018150` | `0x140018150` | 31294 | ✓ |
| `fcn.14000eb40` | `0x14000eb40` | 13704 | ✓ |
| `fcn.14001d5d0` | `0x14001d5d0` | 5850 | ✓ |
| `fcn.140014110` | `0x140014110` | 3368 | ✓ |
| `fcn.140013400` | `0x140013400` | 3344 | ✓ |
| `fcn.1400120d0` | `0x1400120d0` | 3114 | — |
| `fcn.14000df40` | `0x14000df40` | 3057 | — |
| `fcn.140001e60` | `0x140001e60` | 2898 | — |
| `fcn.14001ca10` | `0x14001ca10` | 2386 | — |
| `fcn.14001a5b0` | `0x14001a5b0` | 2376 | — |
| `fcn.140004130` | `0x140004130` | 2084 | — |
| `fcn.140006b80` | `0x140006b80` | 1719 | — |
| `fcn.14000be60` | `0x14000be60` | 1687 | — |
| `fcn.14000c540` | `0x14000c540` | 1654 | — |
| `fcn.140003400` | `0x140003400` | 1555 | — |
| `fcn.140003a20` | `0x140003a20` | 1403 | — |
| `fcn.14001a030` | `0x14001a030` | 1394 | — |
| `fcn.14001bff0` | `0x14001bff0` | 1394 | — |
| `fcn.1400054b0` | `0x1400054b0` | 1287 | — |
| `fcn.140019b90` | `0x140019b90` | 1172 | — |
| `fcn.14001c570` | `0x14001c570` | 1172 | — |
| `fcn.14000a460` | `0x14000a460` | 1158 | — |
| `fcn.140004960` | `0x140004960` | 1133 | — |
| `fcn.140009c00` | `0x140009c00` | 1062 | — |
| `fcn.14000a030` | `0x14000a030` | 1062 | — |
| `fcn.14000ba90` | `0x14000ba90` | 967 | — |
| `fcn.140019080` | `0x140019080` | 945 | — |
| `fcn.14001b380` | `0x14001b380` | 945 | — |
| `fcn.14000cbc0` | `0x14000cbc0` | 924 | — |

### Decompiled Code Files

- [`code/fcn.14000eb40.c`](code/fcn.14000eb40.c)
- [`code/fcn.140013400.c`](code/fcn.140013400.c)
- [`code/fcn.140014110.c`](code/fcn.140014110.c)
- [`code/fcn.140018150.c`](code/fcn.140018150.c)
- [`code/fcn.14001d5d0.c`](code/fcn.14001d5d0.c)
- [`code/fcn.1400202c0.c`](code/fcn.1400202c0.c)

## Behavioral Analysis

This final chunk of disassembly provides the most critical revelation regarding the malware's specific objectives: **targeted session hijacking for messaging platforms, specifically WhatsApp.**

While previous chunks established that this is a sophisticated "Infostealer," this final section confirms it is specifically engineered to steal and "restore" active sessions. This allows an attacker to bypass Multi-Factor Authentication (MFA) and password prompts by simply copying the stolen local database files into their own machine.

---

### Final Comprehensive Analysis: "Session Hijacker" Architecture

#### 1. Target-Specific Data Extraction (WhatsApp Focused)
The code contains extensive logic for navigating deep into browser and application directories to find specific data types. Unlike a general stealer that might just grab passwords, this malware targets the underlying databases of modern web applications:
*   **Targeted Directories:** The code iterates through profiles for **Chrome**, **Microsoft Edge**, and **Bore**. It looks specifically for:
    *   `IndexedDB`: Where modern apps (like WhatsApp Web) store large amounts of local data.
    *   `Local Storage` & `Session Storage`: Used to maintain state and session tokens.
    *   `Cookies`: The primary vehicle for "session hijacking."
*   **Multi-Platform Targeting:** It differentiates between **"Browser Sessions"** (WhatsApp Web) and **"Store Sessions"** (the Microsoft Store/Electron version of the WhatsApp desktop app). This shows a high level of intent to ensure that even if a user doesn't use a web browser, their mobile-linked desktop app is still compromised.

#### 2. Automated "Session Restoration" Logic
A unique and highly advanced feature discovered in this chunk is the creation of batch scripts (`.bat` files) for the attacker:
*   **`RESTORE_BROWSER.bat`**: This script is designed to automate the process of moving stolen folder structures (IndexedDB, Local Storage, Cookies) into a "dummy" profile on the attacker’s machine. It maps out exactly how to make a stolen session look like it belongs in the attacker's browser.
*   **`RESTORE_STORE.bat`**: This targets the specific backend structure of the Windows Store version of WhatsApp (e.g., `EBWebViewDefault`). It includes logic to create directories and copy files into the correct locations so the victim's session "appears" on the attacker's machine.
*   **Automated Environment Setup:** The batch scripts also include commands to find valid paths, move data between temporary folders, and even use `taskkill` to ensure no competing processes (like a running WhatsApp instance) interfere with the data restoration.

#### 3. Attacker "Instruction Manual" (Readme Extraction)
The code generates a large text block (`README.txt`) intended for the attacker's use. This is a hallmark of **professional-grade malware** used by organized cybercrime groups:
*   **Operational Guidance:** It provides instructions on how to choose between the two restoration methods.
*   **Counter-Intelligence:** It explicitly advises the attacker to **"Use VPN from victim's region for best results."** This is a sophisticated tactic designed to bypass geographic-based security alerts that might be triggered when an account suddenly "logs in" from a different country.

#### 4. Correlation with Previous Findings
This chunk connects perfectly with the previous sections:
*   **Headless Browsers (Chunk 2):** These were likely used to interact with the WhatsApp web interface or social media notifications automatically once the session was successfully stolen and "restored" on a secondary machine.
*   **Data Packaging & C2 (Chunk 1/2):** The `.zip` files being exfiltrated are not just "info"—they are functional **session containers**. By zipping the `IndexedDB` and `Cookies`, the attacker can move entire accounts across geographic locations in seconds.

---

### Final Summary of Malicious Behaviors

| Category | Behavior Description | Technical Indicator / Logic Found |
| :--- | :--- | :--- |
| **Targeted Hijacking** | **WhatsApp Session Theft** | Specific logic to target `IndexedDB`, `Local Storage`, and `Cookies` for both Web and Desktop versions of WhatsApp. |
| **Portability** | **Automated Restoration Scripts** | Creation of `.bat` scripts (`RESTORE_BROWSER.bat`) to automate the "injection" of stolen data into an attacker's local environment. |
| **Sophisticated Evasion** | **Geo-Location Awareness** | Inclusion of a `README` instructing the attacker to use VPNs matching the victim's region to bypass security alerts. |
| **Data Packaging** | **Structured Collection** | Packaging multi-format data into `.zip` archives for "one-click" restoration by the threat actor. |
| **Infrastructure** | **Commercial Grade C2** | Use of `voidstealer.net` and multi-tenant headers (`X-Customer-ID`) to manage multiple stolen accounts via a central dashboard. |

---

### Final Evidence of Intent
This is not "script kiddie" malware; it is a **high-value, industrial-scale Information Stealer.** 

The inclusion of the `README` file and the specific automated scripts for "Restoring" sessions indicates that this tool is part of a professional criminal ecosystem. The goal is not just to steal credentials (which can be changed), but to **clone the active session**. By doing so, the attacker gains immediate access to the victim's private communications on WhatsApp without ever needing to know the victim’s phone number or knowing their passcode. 

The specialized handling of "Store" vs "Browser" and the advice regarding regional VPN usage confirms that this is designed for high-volume, professional exploitation where time and success rate are critical.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the observed behaviors of the "Session Hijacker" malware to the relevant MITRE ATT&CK techniques and sub-techniques based on the provided analysis.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1539** | Steal Web Session Cookie | The malware specifically targets `IndexedDB`, `Local Storage`, and `Cookies` to bypass MFA and hijack active WhatsApp sessions. |
| **T1560.001** | Archive Collected Data (Zip Archive) | The malware packages multiple data types into `.zip` files to create "session containers" for easier transport and restoration. |
| **T1059.003** | Windows Command Shell | The creation of `.bat` scripts automates the movement, directory creation, and process termination needed to restore stolen sessions. |
| **T1090** | Proxy | The specific instruction for the attacker to use a VPN to bypass geographic-based security alerts is an effort to evade detection. |
| **T1071** | Application Layer Protocol | Use of a dedicated C2 (`voidstealer.net`) with custom headers like `X-Customer-ID` indicates a structured, multi-tenant infrastructure. |
| **T1005** | Data from Local System | The malware systematically scans and extracts specific data types (browser profiles/app directories) from the victim's local filesystem. |

---

## Indicators of Compromise

Based on the provided string data and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   `voidstealer.net` (C2 Infrastructure)

**File paths / Registry keys**
*   `RESTORE_BROWSER.bat` (Automated restoration script)
*   `RESTORE_STORE.bat` (Automated restoration script for Microsoft Store apps)
*   `README.txt` (Instructional file generated by the malware)
*   `EBWebViewDefault` (Specific directory path utilized to target WhatsApp's store-version data)

**Mutex names / Named pipes**
*   *(None identified)*

**Hashes**
*   *(No standard MD5, SHA1, or SHA256 hashes were present in the provided strings.)*

**Other artifacts**
*   **C2 Communication Header:** `X-Customer-ID` (Used for multi-tenant management of stolen accounts)
*   **Targeted Data Types:** `IndexedDB`, `Local Storage`, `Session Storage`, `Cookies` (Specifically targeted to bypass MFA/passwords)
*   **Tactical Instruction:** "Use VPN from victim's region" (Found in the generated README.txt to evade geographic-based security alerts).

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**IP addresses:**
- `179.43.176.91`

**Domains:**
- `api.ipify.org`
- `blockchain.com`
- `blur.io`
- `btc.com`
- `crypto.com`
- `gate.io`
- `icanhazip.com`
- `voidstealer.net`

---

## Malware Family Classification

Based on the analysis provided, here is the classification:

1. **Malware family:** Infostealer (specifically a "Session Hijacker" variant)
2. **Malware type:** infostealer
3. **Confidence:** High
4. **Key evidence:** 
    *   **Targeted Session Extraction:** The malware specifically targets `IndexedDB`, `Local Storage`, and `Cookies` for both web-based and Microsoft Store versions of WhatsApp to bypass Multi-Factor Authentication (MFA).
    *   **Automated Post-Exfiltration Logic:** The presence of `.bat` scripts (`RESTORE_BROWSER.bat`, `RESTORE_STORE.bat`) and a `README.txt` indicates a professionalized operation designed to move stolen "session containers" to attacker machines seamlessly.
    *   **Sophisticated Evasion/Infrastructure:** Use of multi-tenant C2 headers (`X-Customer-ID`), specific instructions for region-matching VPNs, and the construction of portable zip files confirm this is high-grade, industrial-scale malware rather than a simple script.
