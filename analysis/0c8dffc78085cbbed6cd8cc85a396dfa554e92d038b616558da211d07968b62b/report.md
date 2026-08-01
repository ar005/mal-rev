# Threat Analysis Report

**Generated:** 2026-07-31 16:02 UTC
**Sample:** `0c8dffc78085cbbed6cd8cc85a396dfa554e92d038b616558da211d07968b62b_0c8dffc78085cbbed6cd8cc85a396dfa554e92d038b616558da211d07968b62b.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0c8dffc78085cbbed6cd8cc85a396dfa554e92d038b616558da211d07968b62b_0c8dffc78085cbbed6cd8cc85a396dfa554e92d038b616558da211d07968b62b.exe` |
| File type | PE32 executable for MS Windows 5.00 (GUI), Intel i386, 5 sections |
| Size | 18,944 bytes |
| MD5 | `048b96ef603873e543484d13eff75ada` |
| SHA1 | `f00d28512f510fb28b889155cdbcf97224ec5869` |
| SHA256 | `0c8dffc78085cbbed6cd8cc85a396dfa554e92d038b616558da211d07968b62b` |
| Overall entropy | 6.002 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1779242292 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 8,704 | 5.994 | No |
| `.rdata` | 6,656 | 5.13 | No |
| `.data` | 512 | 1.47 | No |
| `.rsrc` | 1,024 | 5.19 | No |
| `.reloc` | 1,024 | 5.713 | No |

### Imports

**MSVCR90.dll**: `_unlock`, `__dllonexit`, `_lock`, `_onexit`, `?terminate@@YAXXZ`, `_except_handler4_common`, `_invoke_watson`, `_controlfp_s`, `_crt_debugger_hook`, `__set_app_type`, `_encode_pointer`, `__p__fmode`, `__p__commode`, `_adjust_fdiv`, `__setusermatherr`
**WININET.dll**: `InternetCloseHandle`, `InternetOpenUrlA`, `InternetOpenA`, `InternetOpenUrlW`, `InternetOpenW`, `InternetReadFile`
**SHLWAPI.dll**: `StrStrA`, `StrCmpNA`, `PathFileExistsW`
**WS2_32.dll**: `recv`, `select`, `htons`, `gethostbyname`, `inet_addr`, `connect`, `socket`, `closesocket`, `setsockopt`, `shutdown`, `WSAStartup`, `send`
**DNSAPI.dll**: `DnsQuery_A`, `DnsFree`
**KERNEL32.dll**: `GetTickCount`, `lstrlenA`, `GetTimeZoneInformation`, `FileTimeToSystemTime`, `FileTimeToLocalFileTime`, `ExitThread`, `ExitProcess`, `DeleteFileW`, `CreateThread`, `ExpandEnvironmentStringsW`, `GetModuleFileNameW`, `GetLastError`, `CreateMutexA`, `InterlockedExchange`, `InterlockedCompareExchange`
**USER32.dll**: `wsprintfA`, `wsprintfW`

## Extracted Strings

Total strings found: **177** (showing first 100)

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
tMh C@
t"h0e@
t2h,K@
j
XPVj
uhE/@
tVVVVV
%u %s %u %.2u:%.2u:%.2u %s%.2u%.2u
%s, %u %s %u %.2u:%.2u:%.2u %s%.2u%.2u
yahoo.com
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/202.0.4664.110 Safari/537.36
http://icanhazip.com/
[0.0.0.0]
[0.0.0.0]
%s.com
EHLO %s

HELO %s

MAIL FROM: %s

RCPT TO: <%s>

DATA

%s.com
Received: from %s ([%d.%d.%d.%d]) by %s with MailEnable ESMTP; %s

Received: (qmail %s invoked by uid %s); %s

From: %s

To: %s

Subject: %s

Date: %s

Message-ID: <%s.%s@%s>

Mime-Version: 1.0

Content-type: text/plain;


Hello!


Unfortunately, there is some bad news for you.


Some time ago, your device was infected with my private Trojan, R.A.T. (Remote Administration Tool).


If you want to find out more about it, simply use Google.


My Trojan allowed me to access your files and accounts.


Check the sender of this email; I have sent it from your email account!


After that, I removed my malware to leave no traces.


To ensure you read this email, you will receive it multiple times.


I HAVE FOUND NAKED IMAGES OF YOU ON YOUR DEVICE AND HAVE MADE A BACKUP OF THEM!


If you still doubt my serious intentions, it only takes a couple of mouse clicks to share the images with your family, friends, relatives, all email contacts, on social networks, and the darknet.


All you need is $800 USD in Bitcoin (BTC), transferred to my wallet address.


After the transaction is successful, I will proceed to delete everything.


I keep my promises!


You can purchase Bitcoin (BTC) from reputable exchanges here:


http://www.coinbase.com - Payment options: Credit/Debit Cards, Bank Transfers, PayPal (in some regions).

http://www.binance.com - Payment options: Credit/Debit Cards, Bank Transfers, P2P trading, third-party payment providers, and gift cards.

http://www.bitrefill.com - Payment options: Paysafecard, credit/debit cards, crypto, bank transfer, and other gift cards.

http://www.crypto.com - Payment options: Credit/Debit Cards, Bank Transfers, Apple Pay, Google Pay, and more.

http://www.kucoin.com - Payment options: Credit/Debit Cards, Bank Transfer, third-party payment providers, and P2P.

http://www.etoro.com - Payment options: Credit/Debit Cards, Bank Transfers, PayPal.

http://www.kraken.com - Payment options: Bank Transfers, Wire Transfers.


Alternatively, simply Google for other exchanges.


Once purchased, you can send the Bitcoin (BTC) directly to my wallet address or use a wallet application such as Atomic Wallet or Exodus Wallet to manage your transactions.


My Bitcoin (BTC) wallet address is: 1NXeVuYtcVwJ1do2EUS6qJS8FQSPFabxeE


Yes, that's how the wallet address looks. Copy and paste my wallet address; it's case-sensitive.


A piece of advice from me: regularly change all your passwords and update your device with the latest security patches.


Message-ID: %s
%s
.

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
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.004019e0` | `0x4019e0` | 2382 | ✓ |
| `entry0` | `0x402bc7` | 714 | ✓ |
| `fcn.00401490` | `0x401490` | 581 | ✓ |
| `main` | `0x402750` | 262 | ✓ |
| `fcn.004018d0` | `0x4018d0` | 262 | ✓ |
| `fcn.00401230` | `0x401230` | 239 | ✓ |
| `fcn.004017d0` | `0x4017d0` | 224 | ✓ |
| `fcn.00402dd0` | `0x402dd0` | 189 | ✓ |
| `fcn.00402c28` | `0x402c28` | 156 | ✓ |
| `section..text` | `0x401000` | 150 | ✓ |
| `fcn.00402f48` | `0x402f48` | 150 | ✓ |
| `fcn.004016e0` | `0x4016e0` | 127 | ✓ |
| `fcn.004010a0` | `0x4010a0` | 123 | ✓ |
| `fcn.00401760` | `0x401760` | 112 | ✓ |
| `fcn.00401320` | `0x401320` | 104 | ✓ |
| `fcn.00401390` | `0x401390` | 103 | ✓ |
| `fcn.004011c0` | `0x4011c0` | 102 | ✓ |
| `fcn.00401160` | `0x401160` | 81 | ✓ |
| `fcn.00401440` | `0x401440` | 70 | ✓ |
| `fcn.00402e9c` | `0x402e9c` | 69 | ✓ |
| `fcn.00402d80` | `0x402d80` | 68 | ✓ |
| `fcn.00402710` | `0x402710` | 55 | ✓ |
| `fcn.00401400` | `0x401400` | 54 | ✓ |
| `fcn.00401120` | `0x401120` | 54 | ✓ |
| `fcn.00402d40` | `0x402d40` | 53 | ✓ |
| `fcn.00402f1a` | `0x402f1a` | 43 | ✓ |
| `fcn.00402ce4` | `0x402ce4` | 38 | ✓ |
| `fcn.00402ccd` | `0x402ccd` | 23 | ✓ |
| `fcn.004018b0` | `0x4018b0` | 21 | ✓ |
| `fcn.00402350` | `0x402350` | 21 | ✓ |

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
- [`code/fcn.00402350.c`](code/fcn.00402350.c)
- [`code/fcn.00402710.c`](code/fcn.00402710.c)
- [`code/fcn.00402c28.c`](code/fcn.00402c28.c)
- [`code/fcn.00402ccd.c`](code/fcn.00402ccd.c)
- [`code/fcn.00402ce4.c`](code/fcn.00402ce4.c)
- [`code/fcn.00402d40.c`](code/fcn.00402d40.c)
- [`code/fcn.00402d80.c`](code/fcn.00402d80.c)
- [`code/fcn.00402dd0.c`](code/fcn.00402dd0.c)
- [`code/fcn.00402e9c.c`](code/fcn.00402e9c.c)
- [`code/fcn.00402f1a.c`](code/fcn.00402f1a.c)
- [`code/fcn.00402f48.c`](code/fcn.00402f48.c)
- [`code/main.c`](code/main.c)
- [`code/section..text.c`](code/section..text.c)

## Behavioral Analysis

### Overview
The provided code is a **malicious spam/extortion engine**. Its primary purpose is to automate the sending of "Sextortion" emails—a common scam where a victim is falsely informed that they have been infected with malware (specifically a Remote Access Trojan, or R.A.T.) and that explicit images of them have been stolen. The goal is to coerce the user into paying a ransom in Bitcoin ($800) to prevent these images from being shared publicly.

### Core Functionality
*   **SMTP Email Construction:** The code implements a manual SMTP (Simple Mail Transfer Protocol) handshake over TCP sockets. It handles standard commands such as `EHLO/HELO`, `MAIL FROM`, `RCPT TO`, and the `DATA` segment to construct a multi-line email.
*   **Content Generation:** It dynamically builds an extortion message. The messages include various "scare" tactics, links to Bitcoin exchanges (Coinbase, Binance, etc.), and a specific Bitcoin wallet address (`1NXeVuYtcVwJ1do2EUS6qJS8FQSPFabxeE`).
*   **Network Environment Gathering:** 
    *   It uses `WS2_32.dll` for direct socket connections.
    *   It queries `icanhazip.com` via the `WinINet` library to determine the host's public IP address, which it then incorporates into the email headers (e.g., "Received: from...").
*   **Randomization:** The code uses `msvcr90_rand` to generate random values for components like the `Message-ID` and other non-critical header fields, likely to evade simple signature-based detection of identical outgoing emails.

### Suspicious/Malicious Behaviors
*   **Extortion/Scam Activity:** The core payload is a classic "sextortion" scam designed to defraud victims through fear.
*   **Anti-Analysis / Evasion Techniques:** 
    *   **Mutex Check:** In `main`, the code attempts to create a mutex with the unique ID `"a77d7d"`. If the mutex already exists, it exits immediately. This is a common technique to ensure only one instance of the malware runs at a time or to detect if it is being run in certain analysis environments.
    *   **Mark-of-the-Web (MotW) Removal:** The code calls `DeleteFileW` on files ending in `:Zone.Identifier`. This specifically targets and removes "Mark of the Web" metadata that Windows attaches to files downloaded from the internet, helping the binary evade detection or security prompts.
*   **Hidden Networking:** By using raw sockets (`WS2_32`) for SMTP rather than high-level libraries, it attempts to bypass some basic security monitors while still performing standard email communication.

### Notable Techniques & Patterns
*   **Multi-Stage Network Logic:** The binary switches between `WinINet` (for web requests like grabbing the external IP) and `WS2_32` (for the SMTP mail transmission), showing a sophisticated approach to network interaction.
*   **Hardcoded Strings:** A large block of text is hardcoded for the email body, including various Bitcoin payment platforms, which is characteristic of "spam-ware" or botnet modules.
*   **Manual Stack Handling:** The presence of `fcn.00402e9c` and other functions related to stack protection and pointer decoding suggests the code may have been compiled with certain compiler protections or underwent a level of obfuscation/packing before being distributed.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1566** | **Phishing** | The core functionality involves generating and sending "Sextortion" emails containing scam content, threat tactics, and cryptocurrency payment links. |
| **T1071** | **Application Layer Protocol** | The malware manually implements the SMTP protocol over raw sockets to transmit its payload and interact with mail servers. |
| **T1027** | **Indicator Removal on Computer** | The code specifically targets and removes "Mark-of-the-Web" (`:Zone.Identifier`) metadata to evade detection from security software. |
| **T1036** | **System Information Discovery** | The malware queries `icanhazip.com` to retrieve the host's public IP address for inclusion in email headers. |
| **[Defense Evasion]** | **Mutex Check** | The use of a unique mutex (`a77d7d`) is utilized to ensure single-instance execution and potentially detect analysis environments. |
| **[Defense Evasion]** | **Randomization** | The use of `msvcr90_rand` to generate random values for headers (like Message-ID) is intended to evade signature-based detection. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs) categorized by type:

**IP addresses / URLs / Domains**
*   `yahoo.com`
*   `http://icanhazip.com/`
*   `http://www.coinbase.com`
*   `http://www.binance.com`
*   `http://www.bitrefill.com`
*   `http://www.crypto.com`
*   `http://www.kucoin.com`
*   `http://www.etoro.com`
*   `http://www.kraken.com`

**File paths / Registry keys**
*   *(No specific malicious file paths or registry keys were identified in the provided strings.)*

**Mutex names / Named pipes**
*   `a77d7d` (Used as a unique mutex ID to detect existing instances or analysis environments)

**Hashes**
*   *(None identified)*

**Other artifacts**
*   **Bitcoin Wallet Address:** `1NXeVuYtcVwJ1do2EUS6qJS8FQSPFabxeE` (Target for extortion payments)
*   **User-Agent String:** `Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/202.0.4664.110 Safari/537.36`
*   **C2/Communication Patterns:** 
    *   Use of `WinINet` and `WS2_32.dll` for network communication.
    *   Manual SMTP handshake implementation (EHLO, MAIL FROM, RCPT TO, DATA).
    *   Automated "Sextortion" email generation content.
*   **Anti-Analysis Behavior:** 
    *   Targeted removal of `:Zone.Identifier` file suffixes to evade Mark-of-the-Web (MotW) detections.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://icanhazip.com/`
- `http://www.binance.com`
- `http://www.bitrefill.com`
- `http://www.coinbase.com`
- `http://www.crypto.com`
- `http://www.etoro.com`
- `http://www.kraken.com`
- `http://www.kucoin.com`

**Domains:**
- `yahoo.com`

---

## Malware Family Classification

1. **Malware family**: custom (extortion/spam engine)
2. **Malware type**: spambot / extortion tool
3. **Confidence**: High
4. **Key evidence**: 
*   **Automated Extortion Logic:** The core functionality is the construction of "Sextortion" emails using a manual SMTP handshake, hardcoded Bitcoin wallet addresses, and fraudulent scam content to solicit payments from victims.
*   **Evasion Techniques:** The sample implements several anti-analysis features, including Mutex checks to prevent multiple instances, randomized header values to evade signature detection, and the removal of "Mark-of-the-Web" (MotW) metadata.
*   **Sophisticated Networking:** The use of dual-library communication (WinINet for IP discovery and WS2_32 for raw SMTP transmission) suggests a deliberate attempt to perform complex network operations while bypassing standard security filters.
