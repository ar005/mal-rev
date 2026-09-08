# Threat Analysis Report

**Generated:** 2026-09-06 20:38 UTC
**Sample:** `153c1bbfce8fcf4d644a8b7a3843e92e30239d977eb9f4bb21cca7765e48b10d_153c1bbfce8fcf4d644a8b7a3843e92e30239d977eb9f4bb21cca7765e48b10d.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `153c1bbfce8fcf4d644a8b7a3843e92e30239d977eb9f4bb21cca7765e48b10d_153c1bbfce8fcf4d644a8b7a3843e92e30239d977eb9f4bb21cca7765e48b10d.exe` |
| File type | PE32 executable for MS Windows 5.00 (GUI), Intel i386, 5 sections |
| Size | 16,384 bytes |
| MD5 | `a9203e947614ec06570b5753edfc1b68` |
| SHA1 | `b64bb5e5fb565e9f59777ef5025e2bb25a98eb96` |
| SHA256 | `153c1bbfce8fcf4d644a8b7a3843e92e30239d977eb9f4bb21cca7765e48b10d` |
| Overall entropy | 6.066 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1772198961 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 8,192 | 6.08 | No |
| `.rdata` | 4,608 | 5.25 | No |
| `.data` | 512 | 1.455 | No |
| `.rsrc` | 1,024 | 5.194 | No |
| `.reloc` | 1,024 | 5.472 | No |

### Imports

**MSVCR90.dll**: `_unlock`, `__dllonexit`, `_lock`, `_onexit`, `?terminate@@YAXXZ`, `_except_handler4_common`, `_invoke_watson`, `_controlfp_s`, `_crt_debugger_hook`, `__set_app_type`, `_encode_pointer`, `__p__fmode`, `__p__commode`, `_adjust_fdiv`, `__setusermatherr`
**WININET.dll**: `InternetCloseHandle`, `InternetOpenUrlA`, `InternetOpenA`, `InternetOpenUrlW`, `InternetOpenW`, `InternetReadFile`
**SHLWAPI.dll**: `StrStrA`, `StrCmpNA`, `PathFileExistsW`
**WS2_32.dll**: `recv`, `select`, `htons`, `gethostbyname`, `inet_addr`, `connect`, `socket`, `closesocket`, `setsockopt`, `shutdown`, `WSAStartup`, `send`
**DNSAPI.dll**: `DnsQuery_A`, `DnsFree`
**KERNEL32.dll**: `GetTickCount`, `lstrlenA`, `GetTimeZoneInformation`, `FileTimeToSystemTime`, `FileTimeToLocalFileTime`, `ExitThread`, `ExitProcess`, `DeleteFileW`, `CreateThread`, `ExpandEnvironmentStringsW`, `GetModuleFileNameW`, `GetLastError`, `CreateMutexA`, `InterlockedExchange`, `InterlockedCompareExchange`
**USER32.dll**: `wsprintfA`, `wsprintfW`

## Extracted Strings

Total strings found: **156** (showing first 100)

```
!This program cannot be run in DOS mode.
$
5Fw^5Fw^5Fw^
^9Fw^<>
^6Fw^5Fv^TFw^<>
^7Fw^<>
^ Fw^<>
^0Fw^<>
^4Fw^Rich5Fw^
`.rdata
@.data
@.reloc
t"h0U@
j
XPVj
tVVVVV
%u %s %u %.2u:%.2u:%.2u %s%.2u%.2u
%s, %u %s %u %.2u:%.2u:%.2u %s%.2u%.2u
mail.ru
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36
http://icanhazip.com/
[0.0.0.0]
[0.0.0.0]
%s.com
EHLO %s

HELO %s

<JohnBlue@hola.com>
MAIL FROM: %s

RCPT TO: <%s>

DATA

%s.com
Received: from %s ([%d.%d.%d.%d]) by %s with MailEnable ESMTP; %s

Received: (qmail %s invoked by uid %s); %s

From: John Blue %s

To: %s

Subject: %s

Date: %s

Message-ID: <%s.%s@%s>

Mime-Version: 1.0

Content-type: text/plain;


Hello,


Your computer was hacked, and I am aware of your password: 
During routine monitoring, illegal files and activity have been detected on your computer.


These files violate applicable laws and regulations.


To resolve this matter discreetly, you are required to make a payment of $2400 in Bitcoins to the following wallet address: 1ACbLBbnmehCJCdUUrdGvHFC4gsDJbiKYc


Please note that this is how the wallet looks; copy the address exactly as shown, as it is case-sensitive.


Failure to comply within 48 hours will result in all identified information, including evidence of the illegal activity, being forwarded to the appropriate law enforcement authorities for further investigation and action.


strlen
sprintf
strstr
memset
strcat
strcpy
strchr
strtok
fclose
_wfopen
mbstowcs
MSVCR90.dll
_amsg_exit
__getmainargs
_cexit
_XcptFilter
_ismbblead
_acmdln
_initterm
_initterm_e
_configthreadlocale
__setusermatherr
_adjust_fdiv
__p__commode
__p__fmode
_encode_pointer
__set_app_type
?terminate@@YAXXZ
_unlock
__dllonexit
_onexit
_decode_pointer
_except_handler4_common
_invoke_watson
_controlfp_s
_crt_debugger_hook
InternetCloseHandle
InternetReadFile
InternetOpenUrlA
InternetOpenA
InternetOpenUrlW
InternetOpenW
WININET.dll
StrCmpNA
StrStrA
PathFileExistsW
SHLWAPI.dll
WS2_32.dll
DnsFree
DnsQuery_A
DNSAPI.dll
lstrlenA
GetTickCount
GetTimeZoneInformation
FileTimeToSystemTime
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.004019e0` | `0x4019e0` | 1896 | ✓ |
| `entry0` | `0x402a57` | 714 | ✓ |
| `fcn.00401490` | `0x401490` | 581 | ✓ |
| `main` | `0x4025e0` | 270 | ✓ |
| `fcn.004018d0` | `0x4018d0` | 262 | ✓ |
| `fcn.00401230` | `0x401230` | 239 | ✓ |
| `fcn.004017d0` | `0x4017d0` | 224 | ✓ |
| `fcn.00402c60` | `0x402c60` | 189 | ✓ |
| `fcn.00402ab8` | `0x402ab8` | 156 | ✓ |
| `section..text` | `0x401000` | 150 | ✓ |
| `fcn.00402dd8` | `0x402dd8` | 150 | ✓ |
| `fcn.004016e0` | `0x4016e0` | 127 | ✓ |
| `fcn.004010a0` | `0x4010a0` | 123 | ✓ |
| `fcn.00401760` | `0x401760` | 112 | ✓ |
| `fcn.00401320` | `0x401320` | 104 | ✓ |
| `fcn.00401390` | `0x401390` | 103 | ✓ |
| `fcn.004011c0` | `0x4011c0` | 102 | ✓ |
| `fcn.00401160` | `0x401160` | 81 | ✓ |
| `fcn.00401440` | `0x401440` | 70 | ✓ |
| `fcn.00402d2c` | `0x402d2c` | 69 | ✓ |
| `fcn.00402c10` | `0x402c10` | 68 | ✓ |
| `fcn.004025a0` | `0x4025a0` | 55 | ✓ |
| `fcn.00401400` | `0x401400` | 54 | ✓ |
| `fcn.00401120` | `0x401120` | 54 | ✓ |
| `fcn.00402bd0` | `0x402bd0` | 53 | ✓ |
| `fcn.00402daa` | `0x402daa` | 43 | ✓ |
| `fcn.00402b74` | `0x402b74` | 38 | ✓ |
| `fcn.00402b5d` | `0x402b5d` | 23 | ✓ |
| `fcn.004018b0` | `0x4018b0` | 21 | ✓ |
| `fcn.00402170` | `0x402170` | 21 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.004010a0.c`](code/fcn.004010a0.c)
- [`code/fcn.00401120.c`](code/fcn.00401120.c)
- [`code/fcn.00401160.c`](code/fcn.00401160.c)
- [`code/fcn.004011c0.c`](code/fcn.004011c0.c)
- [`code/fcn.00401230.c`](code/fcn.00401230.c)
- [`code/fcn.00401320.c`](code/fcn.00401320.c)
- [`code/fcn.00401390.c`](code/fcn.00401390.c)
- [`code/fcn.00401400.c`](code/fcn.00401400.c)
- [`code/fcn.00401440.c`](code/fcn.00401440.c)
- [`code/fcn.00401490.c`](code/fcn.00401490.c)
- [`code/fcn.004016e0.c`](code/fcn.004016e0.c)
- [`code/fcn.00401760.c`](code/fcn.00401760.c)
- [`code/fcn.004017d0.c`](code/fcn.004017d0.c)
- [`code/fcn.004018b0.c`](code/fcn.004018b0.c)
- [`code/fcn.004018d0.c`](code/fcn.004018d0.c)
- [`code/fcn.004019e0.c`](code/fcn.004019e0.c)
- [`code/fcn.00402170.c`](code/fcn.00402170.c)
- [`code/fcn.004025a0.c`](code/fcn.004025a0.c)
- [`code/fcn.00402ab8.c`](code/fcn.00402ab8.c)
- [`code/fcn.00402b5d.c`](code/fcn.00402b5d.c)
- [`code/fcn.00402b74.c`](code/fcn.00402b74.c)
- [`code/fcn.00402bd0.c`](code/fcn.00402bd0.c)
- [`code/fcn.00402c10.c`](code/fcn.00402c10.c)
- [`code/fcn.00402c60.c`](code/fcn.00402c60.c)
- [`code/fcn.00402d2c.c`](code/fcn.00402d2c.c)
- [`code/fcn.00402daa.c`](code/fcn.00402daa.c)
- [`code/fcn.00402dd8.c`](code/fcn.00402dd8.c)
- [`code/main.c`](code/main.c)
- [`code/section..text.c`](code/section..text.c)

## Behavioral Analysis

Based on the provided disassembly and strings, here is an analysis of the binary sample:

### Core Functionality and Purpose
The primary purpose of this code is to function as **Ransomware/Extortion malware**. Specifically, it is designed to notify a user that their system has been "hacked" and demand payment in Bitcoin. It contains significant infrastructure for networking (SMTP for mailing the ransom note and HTTP for gathering network information).

### Suspicious or Malicious Behavs
The following behaviors are indicative of malicious intent:

*   **Ransomware Communication:** 
    *   The code constructs a multi-line email using the SMTP protocol. It includes standard headers (`MAIL FROM`, `RCPT TO`, `DATA`) and a body containing a ransom demand for **$2400 in Bitcoin** to a specific wallet address (`1ACbLBbnmehCJCdUUrdGvHFC4gsDJbiKYc`).
    *   It uses dynamically generated "Received" headers (using `rand()` functions) to make the outgoing emails appear as if they are coming from various disparate systems, likely to evade automated spam filters or pattern-based security blocks.

*   **Information Gathering & Network Reconnaissance:**
    *   The code connects to `http://icanhazip.com/` (via function `fcn.004017d0`). This is a common technique used by malware to determine the victim's public-facing IP address, which can be used for further targeting or reporting back to a Command and Control (C2) server.
    *   It uses standard User-Agent strings (`Mozilla/5.0...`) to blend in with legitimate web traffic when making these requests.

*   **File Manipulation & Data Downloading:**
    *   Function `fcn.004018d0` utilizes the `WININET` library to connect to a remote URL and download content into a local file. This indicates that the sample may be used as a **downloader** or a "dropper" for additional malicious payloads.

### Notable Techniques & Patterns
*   **Anti-Analysis / Evasion:**
    *   **Mark of the Web Removal:** In `main`, the code calls `GetModuleFileNameW` and then attempts to delete its own `Zone.Identifier` (e.g., `filename:Zone.Identifier`). This is a common technique to remove the "Mark of the Web" metadata, which Windows uses to indicate that a file was downloaded from an untrusted source.
    *   **Mutex Protection:** It creates a unique mutex (`f3f3ff3f33d`) at startup. This ensures only one instance of the malware is running at a time and can also be used to detect if another debugger or monitoring tool is interacting with it.
    *   **Timing-based Check:** Function `fcn.00402dd8` uses `GetTickCount`, `QueryPerformanceCounter`, and `GetSystemTimeAsFileTime`. This is a classic anti-debugging/anti-analysis technique to detect if the code is being executed in a controlled environment or slowed down by an analyst.

*   **Obfuscation & Dynamic Behavior:**
    *   The use of random number generation (`fcn.00401320`, `fcn.00401390`) to generate random strings for email headers suggests an attempt to bypass security heuristics that look for static, repetitive strings in network traffic.

### Summary Table
| Feature | Observation |
| :--- | :--- |
| **Primary Threat** | Ransomware / Extortion |
| **Network Activity** | SMTP (Email), HTTP (IP Discovery/File Download) |
| **Evasion Techniques** | Mutex check, Time-based checks, Mark of the Web removal |
| **Payload Content** | Bitcoin extortion note ($2400_ |
| **Known Targets** | Local system "hacking" claim; Target email infrastructure (mail.ru context) |

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&C framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1486** | Data Encrypted for Impact | The primary purpose of the binary is identified as ransomware, specifically designed to demand a Bitcoin payment. |
| **T1027** | Obfuscated Files or Information | The use of `rand()` functions to generate random strings for email headers is an attempt to bypass security filters and pattern-based detection. |
| **T1016** | System Network Configuration Discovery | The connection to `icanhazip.com` is a common method used by malware to identify the host's public IP address. |
| **T1105** | Ingress Tool Transfer | The use of the `WININET` library to download content from a remote URL indicates functionality as a downloader or dropper. |
| **T1562.001** | Data Manipulation Indicator Removal | The intentional deletion of the `Zone.Identifier` file is used to remove "Mark of the Web" metadata and evade security checks. |
| **T1497** | Virtualization/Sandbox Evasion | The use of `GetTickCount`, `QueryPerformanceCounter`, and `GetSystemTimeAsFileTime` are classic indicators of attempts to detect analysis environments or debuggers. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   `mail.ru` (Domain)
*   `http://icanhazip.com/` (URL - Used for public IP discovery)

**File paths / Registry keys**
*   *(None identified; mentions of "Zone.Identifier" are standard Windows metadata and not specific malicious paths.)*

**Mutex names / Named pipes**
*   `f3f3ff3f33d` (Mutex - Used for single-instance execution/anti-analysis)

**Hashes**
*   *(None identified)*

**Other artifacts**
*   **Bitcoin Wallet:** `1ACbLBbnmehCJCdUUrdGvHFC4gsDJbiKYc` (Extortion payment destination)
*   **User-Agent:** `Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36`
*   **Ransom Amount:** `$2400`
*   **C2 Pattern:** SMTP communication utilizing randomized "Received" headers to evade spam filters.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://icanhazip.com/`

**Domains:**
- `hola.com`
- `mail.ru`

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: ransomware / downloader
3. **Confidence**: High

4. **Key evidence**:
*   **Explicit Extortion Tactics:** The binary contains hardcoded ransom demands ($2400) and a specific Bitcoin wallet address, supported by an automated SMTP routine to send out notification emails. 
*   **Robust Evasion Techniques:** The sample employs multiple anti-analysis methods, including timing-based checks (`GetTickCount`), mutex creation for single instance execution, and the intentional removal of "Mark of the Web" metadata (Zone.Identifier).
*   **Hybrid Functionality:** Beyond its role as ransomware, the use of `WININET` to fetch remote content indicates it also functions as a downloader/loader, capable of pulling additional payloads onto the victim's system.
