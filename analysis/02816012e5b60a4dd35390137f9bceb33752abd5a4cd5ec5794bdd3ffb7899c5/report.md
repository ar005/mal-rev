# Threat Analysis Report

**Generated:** 2026-06-28 07:11 UTC
**Sample:** `02816012e5b60a4dd35390137f9bceb33752abd5a4cd5ec5794bdd3ffb7899c5_02816012e5b60a4dd35390137f9bceb33752abd5a4cd5ec5794bdd3ffb7899c5.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `02816012e5b60a4dd35390137f9bceb33752abd5a4cd5ec5794bdd3ffb7899c5_02816012e5b60a4dd35390137f9bceb33752abd5a4cd5ec5794bdd3ffb7899c5.exe` |
| File type | PE32 executable for MS Windows 5.00 (GUI), Intel i386, 3 sections |
| Size | 87,040 bytes |
| MD5 | `e7467a4d53ae1b82a890e7075f102abf` |
| SHA1 | `2dbc83586cf616a6085a3fc804c01805826b41cf` |
| SHA256 | `02816012e5b60a4dd35390137f9bceb33752abd5a4cd5ec5794bdd3ffb7899c5` |
| Overall entropy | 6.43 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1770549780 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 60,928 | 6.118 | No |
| `.rdata` | 17,408 | 5.711 | No |
| `.data` | 7,680 | 5.58 | No |

### Imports

**WS2_32.dll**: `recv`, `gethostname`, `shutdown`, `recvfrom`, `setsockopt`, `bind`, `closesocket`, `send`, `htons`, `socket`, `connect`, `WSAWaitForMultipleEvents`, `listen`, `WSASocketA`, `WSACreateEvent`
**SHLWAPI.dll**: `StrStrIA`, `PathRemoveFileSpecW`, `StrStrW`, `PathFileExistsW`, `StrChrA`, `PathFindFileNameW`, `StrCmpNIA`, `PathMatchSpecW`
**urlmon.dll**: `URLDownloadToFileW`
**WININET.dll**: `InternetConnectA`, `HttpOpenRequestA`, `HttpSendRequestA`, `InternetOpenA`, `InternetCloseHandle`, `DeleteUrlCacheEntry`, `InternetReadFile`, `InternetCrackUrlA`, `HttpAddRequestHeadersA`, `InternetOpenUrlW`, `InternetOpenW`, `HttpQueryInfoA`, `InternetOpenUrlA`
**ntdll.dll**: `memset`, `iswdigit`, `iswalpha`, `wcsncmp`, `memcpy`, `iswspace`, `NtQueryVirtualMemory`, `RtlUnwind`, `_chkstk`, `_aulldiv`, `wcslen`, `wcscmp`, `_allshl`, `_aullshr`, `strstr`
**msvcrt.dll**: `_vscprintf`, `iswalnum`, `srand`, `rand`
**KERNEL32.dll**: `GetQueuedCompletionStatus`, `PostQueuedCompletionStatus`, `GetSystemInfo`, `MoveFileExW`, `SetEvent`, `CreateProcessW`, `GetFileSizeEx`, `GetLocaleInfoA`, `DeleteCriticalSection`, `GetCurrentThread`, `GetThreadPriority`, `SetThreadPriority`, `GetCurrentProcess`, `DuplicateHandle`, `IsBadReadPtr`
**USER32.dll**: `RegisterClassExW`, `CreateWindowExW`, `GetMessageA`, `TranslateMessage`, `wsprintfW`, `DefWindowProcA`, `ChangeClipboardChain`, `RegisterRawInputDevices`, `GetClipboardData`, `DispatchMessageA`, `OpenClipboard`, `EmptyClipboard`, `CloseClipboard`, `IsClipboardFormatAvailable`, `SendMessageA`
**ADVAPI32.dll**: `CryptGenRandom`, `RegQueryValueExW`, `RegOpenKeyExW`, `RegFlushKey`, `RegSetValueExW`, `CryptAcquireContextW`, `RegCloseKey`, `CryptReleaseContext`, `RegDeleteValueW`
**SHELL32.dll**: `ShellExecuteW`
**ole32.dll**: `CoInitializeEx`, `CoInitialize`, `CoCreateInstance`, `CoUninitialize`
**OLEAUT32.dll**: `SysFreeString`, `SysAllocString`

## Extracted Strings

Total strings found: **369** (showing first 100)

```
!This program cannot be run in DOS mode.
$
 9Rich)
`.rdata
@.data
MPSWU
>ilciuo
L$$QRP
;PCOIu^
>ilciu
F(;F$s
>ilciu2
j=hx`A
9Muxj
uZht$A
umh(%A
umhh%A
VC20XC00U
;t$(v(
kUQPXY]Y[
0x6Df1c493fF422799eA80E1C03531a10DFDFa3Ebe
0xE9bD31C9452E1942Bf1E473067F7e3cd524983CB
0x12eF1d224f72CF0ed28A0dc41c8676A5D4bbDab5
0xC85bF0a9e59e2370FC26d874f0d0ab92A9E85D14
0x8e1086CFb2F7Bc0aDe75E66F1087B8cb81cd9691
0xF24bb5CbDE00Fdf6c03299Af0a96d4d98455c4c7
0x558dD8832C87f3422Cb4af603e5532017EFF9249
0x560AD761B8929eD2aAF2FF6d7B43cC4aE3B7d23f
0x39495fc8716A4694F0169F92540509dDdE21b347
0xdDBc86c6662DF87DA21C7b002fa090F6E6545c62
0xDE5619F2fd7dbDe2E5d53541Ca9e59b73D029B36
0x65D09b0E8FaCd48f8d813856A1EDF51Ec4415a2e
0xD38C661D9a30a56A67595f4f026b5812B2c32bd5
0xb637E9c384B94c92cB87139F776AD34541B69f6d
0xAbc1FBD06144918A5Fe227FA069e68bCa7F03A1B
TLL8bgut26VN4ir2cj7RyEtUt3ChHJpX9F
TMjq6VPX1szmWDEtcw6L5YQ2yMCT65f3Lw
TEHwor6szFH2EvTVjNLzXCLnBpr5bUo62Q
TTi3prs3cfgCuWRntP4TsXt3EEVtP24feT
TThGffNJcA3JJP36iL1fUAqPQr2U9rTxJ3
TFDuTwErXBBhve23cph9d6o5bXYZFWY6zX
TDDVo9sWSKad7if9uKSMX1mJSoMYwJcycB
TU1EUf3tqNDKTm6HSmgsvRPYLtDx97DNFF
TMUdqDjUEDpUJ9zA9RFHmqtmdp9r2xK9oN
TT6f9r5tn7jegM7jiMUw2zUK4qBX4fWYTy
THJoBRFbenoEatwEnLX1eTuaLAHJhaFdgP
TLjcFodME2Ed8Fh9USB1WBFcRqrDwjes7e
TDMysBGndMtr36Zpu1x6ozjJjAMqxccmWX
TBC8sJKnqeZgiwxdJFaxugWa2VspKU2444
TU55ChF5oUHa6NPztdvR5WmXk1cdi5HF69
1Da44vjcoeDY1jnp7asuYhLLHj9zE3QVk9
1DjoxHjPcko38Yaxz3mPneqxroDBadeNRM
1NAMyxyCJF1ama3FmihxAnYwMzcYiL6Qqr
1PguUuYRTwN58umyeAndFy6KCSGHxQYUXw
1PtC4RtUNBjJ5mpjDG5G2PcBdDg1zuXsrf
1BzmrjmKPKSR2hH5BeJySfiVA676E8DYaK
1eh1Y87tfSEcMfX2rZngYmau5PtqgrPAA
1M8r3wmfRkUPjUXbvyex5Ueyweuub67BfN
1B8FF5WwJXNnjkVzxgPkAznVZ8uKb3Watx
15pRnkdX94g5oNPiS3rTeLszP6iy4wbsP4
38qrUcDbbqmh5DuVVYtjQf8fjxxgfREJY1
348U8J2xoXaDLStudokqNYM8YqHhzUkhGE
3AjRi4rS6Q8j8nuy7CBrxkDtHuHRhjSchk
3HjLEtAjzCinDhMDo2jEdAvQNZSnbdc8q4
386jiX2BHpuCrq5CTkirSV6jZPXz8Cuyyb
3LbBmVU8zNUrscxnwfWhBjSAYwZkF9tsNk
3NP9DZGsmTC1FYUMfUqAjL1md6KmpD6ynP
3HjJQ73TeZ5dnKc7U3Cpi74JxRKG8MmaHh
378CAXioEF2qYPBahPUeAAavBGGr36NUn3
3GcQJkfHq7NWgBhhNKjz7uSfM6LzADpLvX
qph44jx8r9k5xeq5cuf958krv3ewrnp5vc6hhdjd3r
mona1qwdqvzuwn6qj7l9xmsfqur2vc7uda0rcpftv9ej
rsXCXBf9SagxV8JfC12d8Bybk84oPdMNN9
QaBvbNAuoU52qCgbqsgoLAbK5P21L6dn5Y
RLefLLmDAZZb5ZynfPMjZ475pQdHVZNz9J
via1qs8zt7jr4sgru6r8dqtdpc93c5d8wmwu8rkz94z
H42AN3K4hbqdprBnJVG8UFQzRZftKJM1EY
Wdv4zK4Fc9D2PJ9aePL9jUmdjvdQeoKV7Q
uhdnHQRJEBxePpLi6YhiS6Kxgct6vG7Q9f
grs1qscr354fdfddglta2hgajrcryl4gqh6ey360d3u
PCsLUHxdx4nFpp5RSYZ6YyJztgYRcErmQk
AULzfBuUAPfCGAXoG5Vq14aP9s6fx3AH4Z
LSPqqgA9VwWqxdrPGBEh1W2hRGkTH8S4qW
MMTWwvFAZG2WWbXLFtmFTWe3vpWMugpgyH
6RXJtDZhpoXSwddTNWfHw1YK28febHjSEPd1jJZCbFzR
UQAbBKbfkiK3Gjo86zgD3yYO5Njf7zxPTEO4JLqN13ruoGDb
4miRRtciy8dvivDC5A4cQWwAwZHYv1TnbDHwGN9TtVv9
4AtjkCVKbtEC3UEN77SQHuH9i1XkzNiRi5VCbA2XGsJh46nJSXfGQn4GjLuupCqmC57Lo7LvKmFUyRfhtJSvKvuw3h9ReKK
XryzFMFVpDUvU7famUGf214EXD3xNUSmQf
X-avax1j8gx8kp4zpldw4rpflyg6zrrl7awv9lg7gq4vt
aPFoyg69vKYCfnKGo1eLBo5XAmoyuZniGc
avax1j8gx8kp4zpldw4rpflyg6zrrl7awv9lg7gq4vt
axelar100le8y8x7w4uls8dhkuvtzten5jyvxgfweewmz
agoric1jm5w8w49p289v3vq9x3kpg69puj57qgp5gwf76
akash125f3mw4xd9htpsq4zj5w5ezm5gags37ylpdqfe
0xcedc0e98c250c555d0420fba7ba45d9941bf577f00c976d6af2058ccde533a36
NASUHUTM7J5HNOJVZ2EULOP6INPNPSE4KN6AQNRI
NN37YENRSEPDYY2AWEX6A2TGEZ3DD6WJ3L3RCRFF63PZI6PVYK6ANRZBLE
SP1GK1GES8EXB6E15KQJ0EM169NQQNDZG8A2GDRZQ
SdRJvZ4LHuGxfsrnRuBcBYzxcQAyKU2MX6
zil19delrukejtr306u0s7ludxrwk434jcl6ghpng3
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00404b20` | `0x404b20` | 3821 | ✓ |
| `fcn.004081d0` | `0x4081d0` | 3708 | ✓ |
| `fcn.00401820` | `0x401820` | 2711 | ✓ |
| `entry0` | `0x407b80` | 1568 | ✓ |
| `fcn.00406b10` | `0x406b10` | 1543 | ✓ |
| `fcn.00404090` | `0x404090` | 1506 | ✓ |
| `fcn.0040abb0` | `0x40abb0` | 1250 | ✓ |
| `fcn.0040bcf0` | `0x40bcf0` | 1001 | ✓ |
| `fcn.00402ec0` | `0x402ec0` | 941 | ✓ |
| `fcn.0040b550` | `0x40b550` | 896 | ✓ |
| `fcn.0040f440` | `0x40f440` | 847 | ✓ |
| `fcn.00402960` | `0x402960` | 757 | ✓ |
| `fcn.00409b70` | `0x409b70` | 716 | ✓ |
| `fcn.00407610` | `0x407610` | 646 | ✓ |
| `fcn.004033a0` | `0x4033a0` | 636 | ✓ |
| `fcn.00403e20` | `0x403e20` | 615 | ✓ |
| `fcn.00406450` | `0x406450` | 597 | ✓ |
| `fcn.0040ed20` | `0x40ed20` | 571 | ✓ |
| `fcn.0040fa19` | `0x40fa19` | 546 | ✓ |
| `fcn.0040e3f0` | `0x40e3f0` | 545 | ✓ |
| `fcn.00404680` | `0x404680` | 531 | ✓ |
| `fcn.00409e40` | `0x409e40` | 515 | ✓ |
| `fcn.00401d60` | `0x401d60` | 495 | ✓ |
| `fcn.00409680` | `0x409680` | 456 | ✓ |
| `fcn.0040cd50` | `0x40cd50` | 454 | ✓ |
| `fcn.0040f010` | `0x40f010` | 443 | ✓ |
| `fcn.00404960` | `0x404960` | 439 | ✓ |
| `fcn.004099b0` | `0x4099b0` | 434 | ✓ |
| `fcn.00409310` | `0x409310` | 432 | ✓ |
| `fcn.00402020` | `0x402020` | 399 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.00401820.c`](code/fcn.00401820.c)
- [`code/fcn.00401d60.c`](code/fcn.00401d60.c)
- [`code/fcn.00402020.c`](code/fcn.00402020.c)
- [`code/fcn.00402960.c`](code/fcn.00402960.c)
- [`code/fcn.00402ec0.c`](code/fcn.00402ec0.c)
- [`code/fcn.004033a0.c`](code/fcn.004033a0.c)
- [`code/fcn.00403e20.c`](code/fcn.00403e20.c)
- [`code/fcn.00404090.c`](code/fcn.00404090.c)
- [`code/fcn.00404680.c`](code/fcn.00404680.c)
- [`code/fcn.00404960.c`](code/fcn.00404960.c)
- [`code/fcn.00404b20.c`](code/fcn.00404b20.c)
- [`code/fcn.00406450.c`](code/fcn.00406450.c)
- [`code/fcn.00406b10.c`](code/fcn.00406b10.c)
- [`code/fcn.00407610.c`](code/fcn.00407610.c)
- [`code/fcn.004081d0.c`](code/fcn.004081d0.c)
- [`code/fcn.00409310.c`](code/fcn.00409310.c)
- [`code/fcn.00409680.c`](code/fcn.00409680.c)
- [`code/fcn.004099b0.c`](code/fcn.004099b0.c)
- [`code/fcn.00409b70.c`](code/fcn.00409b70.c)
- [`code/fcn.00409e40.c`](code/fcn.00409e40.c)
- [`code/fcn.0040abb0.c`](code/fcn.0040abb0.c)
- [`code/fcn.0040b550.c`](code/fcn.0040b550.c)
- [`code/fcn.0040bcf0.c`](code/fcn.0040bcf0.c)
- [`code/fcn.0040cd50.c`](code/fcn.0040cd50.c)
- [`code/fcn.0040e3f0.c`](code/fcn.0040e3f0.c)
- [`code/fcn.0040ed20.c`](code/fcn.0040ed20.c)
- [`code/fcn.0040f010.c`](code/fcn.0040f010.c)
- [`code/fcn.0040f440.c`](code/fcn.0040f440.c)
- [`code/fcn.0040fa19.c`](code/fcn.0040fa19.c)

## Behavioral Analysis

### Malware Analysis Report

#### **Core Functionality and Purpose**
The binary is a multi-stage **malicious downloader/trojan**. Its primary purpose is to establish persistence on a local machine, bypass network security (specifically router firewalls), and download additional components or payloads from remote servers. It masquerades as system services by using names like `DrvSvcsrMgr._exe` and `sysmrvhost.exe`.

#### **Suspicious and Malicious Behaviors**
*   **Persistence and Masquerading:** 
    *   The code identifies its own filename and checks if it matches "expected" system-like names (e.g., `DrvSvcsrMgr.exe`). 
    *   It performs a series of **file copies** to various standard directories: `%USERPROFILE%`, `%windir%` (Windows directory), and `%appdata%`.
    *   In each location, it renames itself to `sysmrvhost.exe` and modifies the Windows Registry to associate these files with "Windows Settings," ensuring the malware starts automatically on boot.
*   **Self-Deletion/Stealth:** 
    *   After creating its copies in more permanent locations, the binary calls `DeleteFileW` on its original path to remove traces of the initial dropper from the disk.
*   **Firewall & NAT Bypassing (UPnP):** 
    *   The code contains a significant amount of logic dedicated to **Universal Plug and Play (UPnP)**. 
    *   It checks if the local machine is behind a router (by looking for private IP ranges like `192.x`, `10.x`, etc.) and then attempts to send SOAP requests to the gateway to **open ports** on the router (`AddPortMapping`). This allows the attacker to establish an inbound connection to the infected machine from the internet.
*   **Network Communication & Downloader:** 
    *   The code utilizes the `WinINet` library and `urlmon.dll` (e.g., `InternetOpenW`, `HttpSendRequestA`, `URLDownloadToFileW`) to connect to remote servers and download files to the local disk.
*   **Encryption & Obfuscation:** 
    *   It uses an extensive **string decryption/de-obfuscation routine** (`fcn.00404b20`). It checks specific character values and lengths of internal strings before mapping them to the long, randomized-looking data blocks seen in the string dump (e.g., `qph44j...`, `mona1qw...`). This is designed to hide C2 addresses and internal configuration from simple static analysis.

#### **Notable Techniques and Patterns**
*   **Multi-Threading:** The entry point (`entry0`) spawns several threads at different offsets (e.g., `0x407a20`, `0x405c70`). This suggests a modular design where different threads handle separate tasks like networking, file system manipulation, and persistent monitoring.
*   **Script-like Behavior:** The presence of various cryptocurrency addresses in the strings (e.g., "bitcoincash", "ronin") may suggest functionality for ransom notes or instructions for payment if used as a precursor to ransomware.
*   **Resource Triage:** The use of `CreateMutexA` with a hardcoded name (`79o0pl7gf`) is a standard technique to ensure only one instance of the malware runs at a time.
*   **Decoding Routine:** `fcn.004081d0` uses intensive bitwise operations (XOR, shifts) and arithmetic. This indicates that data fetched from the network or hidden in the binary's resources is decrypted into memory only when needed to evade detection by heuristic scanners.

### Summary Checklist
*   **Persistence:** Yes (Registry + Multiple Copy Locations)
*   **Anti-Analysis:** Yes (String Obfuscation, Self-Deletion)
*   **Network Communication:** Yes (HTTP/WinINet + UPnP Port Mapping)
*   **Downloader Behavior:** Yes (Active fetching of remote files)
*   **Information Stealing / Command & Control:** Likely (Infrastructure for a backdoor is present)

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed activities to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1546.003** | Boot or Logon Autostart Execution: Registry Run Keys/Startup Folder | The malware modifies the Windows Registry to associate its files with "Windows Settings" and ensure it starts automatically upon boot. |
| **T1036.005** | Masquerading: System Services | The malware uses system-like filenames (e.g., `DrvSvcsrMgr` and `sysmrvhost`) to blend in with legitimate operating system services. |
| **T1070.004** | Indicator Removal on Host: File Deletion | The binary calls `DeleteFileW` to remove the initial dropper from the disk after successfully migrating its copies. |
| **T1105** | Ingress Tool Transfer | The malware utilizes `WinINet` and `urlmon.dll` functions (like `URLDownloadToFileW`) to download additional components from remote servers. |
| **T1027** | Obfuscated Files or Information | The code includes a heavy decryption routine using XOR, bitwise shifts, and arithmetic to hide C2 addresses and configuration data from analysis. |

***Note on Network Behavior:** While the UPnP/Port Mapping behavior is an active technique for bypassing network security controls (specifically NAT/Firewall evasion), there is no single specific MITRE ATT&C sub-technique exclusively for "UPnP." It is often categorized under general "Network Security Control Bypass" or associated with infrastructure preparation.*

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs) categorized by type:

**IP addresses / URLs / Domains**
*   `178.16.54.109`
*   `195.178.136.19`
*   `www.update.microsoft.com` (Note: Likely used as a decoy or to blend in with legitimate traffic)

**File paths / Registry keys**
*   `DrvSvcsrMgr._exe` (Malicious masquerading filename)
*   `sysmrvhost.exe` (Malicious masquerading filename)

**Mutex names / Named pipes**
*   `79o0pl7gf`

**Hashes**
*(No standard MD5, SHA-1, or SHA-256 hashes were identified in the provided strings; several long hex strings appear to be internal decryption keys/keys for obfuscation routines rather than file hashes.)*

**Other artifacts**
*   **User Agent:** `Mozilla/4.0 (compatible; UPnP/1.0; Windows 9x)`
*   **Cryptocurrency Addresses:**
    *   `qph44jx8r9k5xeq5cuf958krv3ewrnp5vc6hhdjd3r` (Bitcoin Cash)
    *   `a77fa3ea6e09a5f3fbfcb2a42fe21b5cf0ecdd1a` (Ronin)
*   **UPnP SOAP Actions:**
    *   `urn:schemas-upnp-org:service:WANIPConnection:1#GetExternalIPAddress`
    *   `urn:schemas-upnp-org:service:WANIPConnection:1#AddPortMapping`
    *   `urn:schemas-upnp-org:service:WANIPConnection:1#DeletePortMapping`

---

## Malware Family Classification

Based on the analysis provided, here is the classification for the sample:

1. **Malware family:** Unknown
2. **Malware type:** Downloader / Backdoor
3. **Confidence:** High

**Key evidence:**
*   **Multi-stage Downloader Behavior:** The binary is explicitly identified as a multi-stage downloader that uses `WinINet` and `urlmon.dll` to fetch additional payloads, while employing self-deletion and sophisticated string obfuscation (XOR/Bitwise) to hide its C2 infrastructure.
*   **Network Evasion & Persistence:** The inclusion of **UPnP Port Mapping** logic is a high-confidence indicator of intent to bypass firewall/NAT restrictions for remote access, which is characteristic of backdoors and botnet components. 
*   **Masquerading & Persistence:** The malware actively attempts to blend in with the operating system by renaming files to system-like names (e.g., `sysmrvhost.exe`) and modifying Registry keys to ensure long-term persistence on the host.
