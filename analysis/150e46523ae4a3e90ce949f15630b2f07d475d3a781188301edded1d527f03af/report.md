# Threat Analysis Report

**Generated:** 2026-09-06 18:32 UTC
**Sample:** `150e46523ae4a3e90ce949f15630b2f07d475d3a781188301edded1d527f03af_150e46523ae4a3e90ce949f15630b2f07d475d3a781188301edded1d527f03af.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `150e46523ae4a3e90ce949f15630b2f07d475d3a781188301edded1d527f03af_150e46523ae4a3e90ce949f15630b2f07d475d3a781188301edded1d527f03af.exe` |
| File type | PE32 executable for MS Windows 5.00 (GUI), Intel i386, 5 sections |
| Size | 23,552 bytes |
| MD5 | `cd4c600f913d5049c38f9fee1f2dc69d` |
| SHA1 | `00efa058d9014a7893410b20dd34e5937fded0f5` |
| SHA256 | `150e46523ae4a3e90ce949f15630b2f07d475d3a781188301edded1d527f03af` |
| Overall entropy | 6.081 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1779468961 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 12,288 | 6.064 | No |
| `.rdata` | 7,168 | 5.171 | No |
| `.data` | 512 | 1.432 | No |
| `.rsrc` | 1,024 | 5.19 | No |
| `.reloc` | 1,536 | 4.729 | No |

### Imports

**MSVCR90.dll**: `_lock`, `_onexit`, `_decode_pointer`, `__dllonexit`, `_invoke_watson`, `_controlfp_s`, `_crt_debugger_hook`, `fclose`, `_unlock`, `?terminate@@YAXXZ`, `__set_app_type`, `_encode_pointer`, `__p__fmode`, `__p__commode`, `_adjust_fdiv`
**WS2_32.dll**: `WSAStartup`, `shutdown`, `closesocket`, `socket`, `connect`, `inet_addr`, `gethostbyname`, `select`, `recv`, `send`, `htons`, `setsockopt`
**WININET.dll**: `InternetOpenW`, `InternetOpenUrlW`, `InternetOpenA`, `InternetOpenUrlA`, `InternetReadFile`, `InternetCloseHandle`
**SHLWAPI.dll**: `PathFileExistsW`, `StrStrA`, `StrCmpNA`
**DNSAPI.dll**: `DnsFree`, `DnsQuery_A`
**KERNEL32.dll**: `CloseHandle`, `Sleep`, `GetLocalTime`, `WriteFile`, `FileTimeToSystemTime`, `GetTimeZoneInformation`, `GetTickCount`, `lstrlenA`, `CreateFileW`, `FileTimeToLocalFileTime`, `CreateMutexA`, `ExitProcess`, `CreateThread`, `DeleteFileW`, `ExpandEnvironmentStringsW`
**USER32.dll**: `wsprintfA`, `wsprintfW`

## Extracted Strings

Total strings found: **160** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
@.reloc
t"h0e@
tbh4P@
tJh8P@
t2h<P@
j
XPVj
tVVVVV
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36
http://icanhazip.com/
[0.0.0.0]
[0.0.0.0]
%u %s %u %.2u:%.2u:%.2u %s%.2u%.2u
%s, %u %s %u %.2u:%.2u:%.2u %s%.2u%.2u
yahoo.com
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

%s%s%s
Content-Type: multipart/mixed; boundary= "%s"


--%s

Content-Type: text/plain;


Hello!

Unfortunately, there is some bad news for you.

Some time ago, your device was infected with my private Trojan, R.A.T. (Remote Administration Tool).

If you want to find out more about it, simply use Google.

My Trojan allowed me to access your files, accounts, and your camera.

Check the sender of this email; I have sent it from your email account!

To ensure you read this email, you will receive it multiple times.

I RECORDED YOU MASTURBATING!

In the attachment, you will find a small screensaver file containing a scene where you are masturbating.

After that, I removed my malware to leave no traces.

If you still doubt my serious intentions, it only takes a couple of mouse clicks to share the video of you masturbating with your family, friends, relatives, all email contacts, on social networks, and the darknet.

All you need is $1200 USD in Bitcoin (BTC), transferred to my wallet address.

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

My Bitcoin (BTC) wallet address is: 1G1zmqks1vd9V3SdxCY71Hv9C7rHBLQbCY

Yes, that's how the wallet address looks. Copy and paste my wallet address; it's case-sensitive.

A piece of advice from me: regularly change all your passwords and update your device with the latest security patches.


--%s

Content-Type: application/zip

Content-Transfer-Encoding: base64

Content-Disposition: attachment; filename= "Pervert.zip"


--%s--

Pervert.scr
fclose
fscanf
fprintf
_wfopen
strlen
strstr
sprintf
memset
strchr
strtok
strcpy
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
WS2_32.dll
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
DnsFree
DnsQuery_A
DNSAPI.dll
lstrlenA
GetTickCount
GetTimeZoneInformation
FileTimeToSystemTime
FileTimeToLocalFileTime
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00401d90` | `0x401d90` | 2486 | ✓ |
| `section..text` | `0x401000` | 937 | ✓ |
| `fcn.004030f0` | `0x4030f0` | 894 | ✓ |
| `entry0` | `0x403927` | 714 | ✓ |
| `fcn.00402ea0` | `0x402ea0` | 582 | ✓ |
| `fcn.00401940` | `0x401940` | 581 | ✓ |
| `main` | `0x402d70` | 295 | ✓ |
| `fcn.00401c80` | `0x401c80` | 262 | ✓ |
| `fcn.004016e0` | `0x4016e0` | 239 | ✓ |
| `fcn.004014d0` | `0x4014d0` | 224 | ✓ |
| `fcn.00403b30` | `0x403b30` | 189 | ✓ |
| `fcn.00403470` | `0x403470` | 174 | ✓ |
| `fcn.00403988` | `0x403988` | 156 | ✓ |
| `fcn.004013b0` | `0x4013b0` | 150 | ✓ |
| `fcn.00403ca8` | `0x403ca8` | 150 | ✓ |
| `fcn.00403520` | `0x403520` | 144 | ✓ |
| `fcn.00401b90` | `0x401b90` | 127 | ✓ |
| `fcn.00401450` | `0x401450` | 123 | ✓ |
| `fcn.00401c10` | `0x401c10` | 112 | ✓ |
| `fcn.004017d0` | `0x4017d0` | 104 | ✓ |
| `fcn.00401840` | `0x401840` | 103 | ✓ |
| `fcn.00401670` | `0x401670` | 102 | ✓ |
| `fcn.00401610` | `0x401610` | 81 | ✓ |
| `fcn.004018f0` | `0x4018f0` | 70 | ✓ |
| `fcn.00403bfc` | `0x403bfc` | 69 | ✓ |
| `fcn.00403ae0` | `0x403ae0` | 68 | ✓ |
| `fcn.00402d30` | `0x402d30` | 55 | ✓ |
| `fcn.004018b0` | `0x4018b0` | 54 | ✓ |
| `fcn.004015d0` | `0x4015d0` | 54 | ✓ |
| `fcn.00403aa0` | `0x403aa0` | 53 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.004013b0.c`](code/fcn.004013b0.c)
- [`code/fcn.00401450.c`](code/fcn.00401450.c)
- [`code/fcn.004014d0.c`](code/fcn.004014d0.c)
- [`code/fcn.004015d0.c`](code/fcn.004015d0.c)
- [`code/fcn.00401610.c`](code/fcn.00401610.c)
- [`code/fcn.00401670.c`](code/fcn.00401670.c)
- [`code/fcn.004016e0.c`](code/fcn.004016e0.c)
- [`code/fcn.004017d0.c`](code/fcn.004017d0.c)
- [`code/fcn.00401840.c`](code/fcn.00401840.c)
- [`code/fcn.004018b0.c`](code/fcn.004018b0.c)
- [`code/fcn.004018f0.c`](code/fcn.004018f0.c)
- [`code/fcn.00401940.c`](code/fcn.00401940.c)
- [`code/fcn.00401b90.c`](code/fcn.00401b90.c)
- [`code/fcn.00401c10.c`](code/fcn.00401c10.c)
- [`code/fcn.00401c80.c`](code/fcn.00401c80.c)
- [`code/fcn.00401d90.c`](code/fcn.00401d90.c)
- [`code/fcn.00402d30.c`](code/fcn.00402d30.c)
- [`code/fcn.00402ea0.c`](code/fcn.00402ea0.c)
- [`code/fcn.004030f0.c`](code/fcn.004030f0.c)
- [`code/fcn.00403470.c`](code/fcn.00403470.c)
- [`code/fcn.00403520.c`](code/fcn.00403520.c)
- [`code/fcn.00403988.c`](code/fcn.00403988.c)
- [`code/fcn.00403aa0.c`](code/fcn.00403aa0.c)
- [`code/fcn.00403ae0.c`](code/fcn.00403ae0.c)
- [`code/fcn.00403b30.c`](code/fcn.00403b30.c)
- [`code/fcn.00403bfc.c`](code/fcn.00403bfc.c)
- [`code/fcn.00403ca8.c`](code/fcn.00403ca8.c)
- [`code/main.c`](code/main.c)
- [`code/section..text.c`](code/section..text.c)

## Behavioral Analysis

This is an analysis of the provided disassembly and string data.

### Core Functionality and Purpose
The binary's primary purpose is to act as a **Malicious Email Spammer** (specifically for "Sextortion" scams). It is designed to automate the process of connecting to a Mail Transfer Agent (MTA) via SMTP protocols to send high-volume, threatening emails to victims. The email content claims the victim has been recorded in a compromising manner and demands payment in Bitcoin to prevent the release of said footage.

### Suspicious or Malicious Behaviors
*   **Automated SMTP Interaction:** The code contains a large switch-case block that implements a full SMTP handshake:
    *   It interacts with server banners (checking for "ESMTP").
    *   It sends standard commands like `EHLO/HELO`, `MAIL FROM`, and `RCPT TO`.
    *   It manages various headers including `Subject`, `Date`, and `Message-ID`.
*   **Sextortion Scam Delivery:** The hardcoded string (starting at `0x4045f4`) is a classic "sextortion" script. It includes:
    *   Extreme threats regarding "recording" the user.
    *   A demand for **$1200 USD in Bitcoin**.
    *   Links to several cryptocurrency exchanges (Coinbase, Binance, etc.).
    *   An attachment titled `Pervert.zip` which likely contains a fake payload or a script to further compromise the victim.
*   **Evasion of "Mark of the Web"**: In the `main` function, the code specifically targets and deletes the `.Zone.Identifier` file associated with itself. This is a common technique used by malware to remove the metadata that tells Windows a file was downloaded from the internet (the "Mark of the Web").
*   **Anti-Analysis / Single Instance:** The use of `CreateMutexA` with a specific string (`dd3ff3f3f`) ensures that only one instance of the program runs at a time. This is often used to prevent researchers from running multiple instances or to ensure the malware doesn't "clash" with itself during a spam campaign.
*   **De-obfuscation on Execution:** The function `fcn.004013b0` performs a XOR/XOR-like operation on strings. This indicates that several internal strings are kept in an encrypted state until the moment they are needed, making it harder for static analysis tools to find malicious content without running the binary.

### Notable Techniques or Patterns
*   **Raw Socket Usage:** Instead of using high-level mail libraries, it uses `WS2_32.dll` directly to manage connections and `select` (via `fcn.004016e0`) to handle non-blocking I/O on the network.
*   **Information Gathering:** It includes a function (`fcn.004014d0`) that calls `icanhazip.com`. This is used to determine the local IP address, which can be used by the attacker to validate where the spamming bot is operating from.
*   **Data Decryption/Transformation:** The functions `fcn.00403520` and `fcn.00402ea0` suggest a routine for processing or "unpacking" data (potentially the email body or attachments) into memory before transmission or file writing.
*   **Fake Identity Generation:** The code uses `fcn.00401840` to generate random alphanumeric strings, likely used to forge sender information or other headers to bypass simple spam filters.

### Summary for Incident Response
This binary is a **malicious mailer**. If found on a system, it indicates that the machine is being used as a "bot" to send out fraudulent sextortion emails. The presence of `_Zone.Identifier` deletion and mutex checks suggests an intentional effort to stay resident while performing automated spam tasks.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1071.005 | Application Layer Protocol: SMTP | The malware utilizes the SMTP protocol and a manual handshake process to automate the delivery of spam emails. |
| T1027 | Obfuscated Files or Information | The use of XOR operations on internal strings and the removal of `.Zone.Identifier` files are used to hide malicious content and origin from analysis. |
| T1036 | Masquerading | The generation of random alphanumeric strings is used to forge sender information and mimic legitimate email headers to bypass filters. |
| T1082 | System Information Discovery | The query to `icanhazip.com` identifies the system's public IP address to determine the bot's current network environment. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the identified Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   `http://icanhazip.com/` (Used for local IP identification)
*   `http://www.coinbase.com`
*   `http://www.binance.com`
*   `http://www.bitrefill.com`
*   `http://www.crypto.com`
*   `http://www.kucoin.com`
*   `http://www.etoro.com`
*   `http://www.kraken.com`

**File paths / Registry keys**
*   `Pervert.zip` (Malicious archive name)
*   `Pervert.scr` (Executable file/script)
*   `.Zone.Identifier` (Targeted for deletion to remove "Mark of the Web")

**Mutex names / Named pipes**
*   `dd3ff3f3f` (Used for anti-analysis and single-instance enforcement)

**Hashes**
*   *(None found in provided strings)*

**Other artifacts**
*   **User Agent:** `Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36`
*   **Bitcoin Wallet:** `1G1zmqks1vd9V3SdxCY71Hv9C7rHBLQbCY`
*   **C2 Pattern:** Automated SMTP interaction using standard commands (`EHLO`, `MAIL FROM`, `RCPT TO`) to distribute "sextortion" spam.
*   **Evasion Technique:** Deletion of `.Zone.Identifier` files to hide the origin of the file from Windows security features.

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

1. **Malware family**: custom (Sextortion Mailer)
2. **Malware type**: bot
3. **Confidence**: High
4. **Key evidence**: 
*   **Automated SMTP Infrastructure:** The binary implements a full manual SMTP handshake (EHLO, MAIL FROM, RCPT TO) to automate the delivery of high-volume "sextortion" emails including specific Bitcoin payment demands and malicious filenames (`Pervert.zip`).
*   **Evasion & Anti-Analysis:** It employs several techniques to hinder detection, including XOR de-obfuscation for internal strings, `CreateMutexA` for single-instance control, and the intentional deletion of `.Zone.Identifier` files to remove "Mark of the Web" metadata.
*   **Information Harvesting/Tracking:** The inclusion of a check against `icanhazip.com` indicates the malware is designed to operate as part of a botnet where it validates its own network environment for the purposes of automated spam distribution.
