# Threat Analysis Report

**Generated:** 2026-07-25 23:15 UTC
**Sample:** `0b3bca24417a215c0c33a2bf4fd3ffb61bdd5f25c79ada55cce359a5c5c3acaa_0b3bca24417a215c0c33a2bf4fd3ffb61bdd5f25c79ada55cce359a5c5c3acaa.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0b3bca24417a215c0c33a2bf4fd3ffb61bdd5f25c79ada55cce359a5c5c3acaa_0b3bca24417a215c0c33a2bf4fd3ffb61bdd5f25c79ada55cce359a5c5c3acaa.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64 Mono/.Net assembly, 2 sections |
| Size | 252,416 bytes |
| MD5 | `2a45b21bb07456351db2b3bdcafa83d5` |
| SHA1 | `b0d4db9a2f34b1e679444f6e89890d35c7213f76` |
| SHA256 | `0b3bca24417a215c0c33a2bf4fd3ffb61bdd5f25c79ada55cce359a5c5c3acaa` |
| Overall entropy | 5.82 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 2392541779 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 250,368 | 5.832 | No |
| `.rsrc` | 1,536 | 4.061 | No |

## Extracted Strings

Total strings found: **1666** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc
3DC5CA39
 iciNWq
Ze2Zh@
A4x{%`
>3b$;"
BFUa.X
	-f3F2
|K=
r9$|
Y:D
5>
w``u N
expand 32-byte k

,=re	

,Or|

-A	(!

,z	(I
j[ri6

&	r	G

&	r1G
	,j(F

-j	(C

,;r1}
+%-&r
v4.0.30319
#Strings
 7W9
+
 $ + 1 J U | 
!"!2!:!@!p!
#"#)#>#Y#z#
$9$T$[$q$
%1%:%q%
&'&0&;&[&
&
'H'Q'^'j's'
)()/)6);)L)T)d)j)
)*%*/*<*\*~*
*%+B+h+
+.,3,Y,
.-/;/A/I/V/^/g/?
p9C9P9z9,9[969g9Y
$)%V%f&,':'['p(
__StaticArrayInitTypeSize=10
_masterKeyCacheV10
ComputeMasterKeyV10
<ProfileCollect>b__10
masterv10
masterKey10
__StaticArrayInitTypeSize=20
_masterKeyCacheV20
ComputeMasterKeyV20
masterv20
masterKey20
2E69DC77B5DCFCCF57DD14F7E8BC6846C81B48D65C372C8970A25FA856421FE0
FA1AD270B23BA640E88EE7F51CC9C0C1A6C6BB1F2B9025682A7D30FB3BDA64F0
<>9__10_0
<Collect>b__10_0
<>c__DisplayClass20_0
<>9__0_0
<Collect>b__0_0
<>c__DisplayClass0_0
<Collect>g__AppendFound|0_0
<>9__1_0
<Key3Database>b__1_0
<Collect>b__1_0
<StringToByteArray>b__1_0
<>c__DisplayClass1_0
<>c__DisplayClass12_0
<>9__2_0
<DecryptPassword>b__2_0
<Sessions>b__2_0
<GetChromeWallets>b__2_0
<>c__DisplayClass2_0
<>c__DisplayClass13_0
<>9__3_0
<TryExportAndParseProfiles>b__3_0
<Collect>b__3_0
<>c__DisplayClass3_0
<>c__DisplayClass14_0
<>9__4_0
<MasterKeyV20>b__4_0
<GenerateString>b__4_0
<BuildDrivesSection>b__4_0
<>c__DisplayClass4_0
<>c__DisplayClass15_0
<>9__5_0
<Main>b__5_0
<>c__DisplayClass5_0
<>c__DisplayClass16_0
<>9__6_0
<MasterKeyV10>b__6_0
<BuildCache>b__6_0
<GenerateDomainDetectsFile>b__6_0
<>c__DisplayClass6_0
<>c__DisplayClass17_0
<>c__DisplayClass7_0
<>c__DisplayClass18_0
<>c__DisplayClass19_0
<>c__DisplayClass9_0
<>9__0
<FindInAppData>b__0
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `sym.__c..cctor_17` | `0x1400044ed` | 252692 | ✓ |
| `entry0` | `0x14001d598` | 150120 | ✓ |
| `method.CvMega.Helper.SimpleEncryptor.Decrypt` | `0x1400046c3` | 130602 | ✓ |
| `method.CvMega.Helper.SimpleEncryptor.XorEncrypt` | `0x14001e808` | 60816 | ✓ |
| `method.Intelix.Targets.Browsers.CryptoChromium..ctor` | `0x14000e170` | 2916 | ✓ |
| `method.Intelix.Targets.Device.ScreenShot.Collect` | `0x1400091f0` | 2724 | ✓ |
| `method.Intelix.Helper.Data.Counter.Collect` | `0x14001bcb4` | 2600 | ✓ |
| `method.Intelix.Targets.Games.Steam.Collect` | `0x140007868` | 1804 | ✓ |
| `method._Main_d__5.MoveNext` | `0x14001d678` | 1780 | ✓ |
| `method.Intelix.Helper.Data.Paths..cctor` | `0x14001ca90` | 1724 | ✓ |
| `method.Intelix.Targets.Crypto.CryptoDesktop..cctor` | `0x14000b1f4` | 1652 | ✓ |
| `method.Intelix.Targets.Applications.RDCMan.Collect` | `0x1400125d4` | 1164 | ✓ |
| `method.Intelix.Helper.Sql.SqLite.ReadTableFromOffset` | `0x140016234` | 1160 | ✓ |
| `method.Intelix.Helper.Sql.SqLite.ReadMasterTable` | `0x1400166bc` | 1112 | ✓ |
| `method.Intelix.Targets.Applications.Sunlogin.Collect` | `0x140012d48` | 1104 | ✓ |
| `method.Intelix.Helper.Data.ConsolidatedFilesGenerator.GenerateUserInformationFile` | `0x14001b07c` | 1096 | ✓ |
| `method.Intelix.Helper.Data.ConsolidatedFilesGenerator.GenerateDomainDetectsFile` | `0x14001b690` | 1076 | ✓ |
| `method.Intelix.Helper.Encrypted.NssDumpMasterKey.Key4Database` | `0x140019b90` | 1072 | ✓ |
| `method._SendToTelegram_d__6.MoveNext` | `0x14001dd6c` | 1044 | ✓ |
| `method.Intelix.Targets.Browsers.Chromium.ProfileCollect` | `0x14000bf9c` | 1032 | ✓ |
| `method.CvMega.Program..cctor` | `0x14001d1f4` | 932 | ✓ |
| `method.Intelix.Targets.Crypto.Grabber..ctor` | `0x14000ba20` | 920 | ✓ |
| `method.__c__DisplayClass18_0._YandexGetCard_b__0` | `0x14000d9f4` | 888 | ✓ |
| `method.Intelix.Helper.Encrypted.NssDumpMasterKey.Key3Database` | `0x140019fc0` | 856 | ✓ |
| `method.Intelix.Targets.Device.WifiKey.TryExportAndParseProfiles` | `0x14000aa4c` | 792 | ✓ |
| `method.Intelix.Targets.Device.ProcessDump.Collect` | `0x140008ba0` | 740 | ✓ |
| `method.Intelix.Targets.Games.Minecraft.Collect` | `0x1400072a4` | 720 | ✓ |
| `method.Intelix.Helper.Encrypted.Asn1Der.Parse` | `0x140017d20` | 716 | ✓ |
| `method.Intelix.Targets.Applications.FTPRush.Collect` | `0x1400110d0` | 708 | ✓ |
| `method.Intelix.Targets.Applications.Rdp.Collect` | `0x140012a98` | 688 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/method.CvMega.Helper.SimpleEncryptor.Decrypt.c`](code/method.CvMega.Helper.SimpleEncryptor.Decrypt.c)
- [`code/method.CvMega.Helper.SimpleEncryptor.XorEncrypt.c`](code/method.CvMega.Helper.SimpleEncryptor.XorEncrypt.c)
- [`code/method.CvMega.Program..cctor.c`](code/method.CvMega.Program..cctor.c)
- [`code/method.Intelix.Helper.Data.ConsolidatedFilesGenerator.GenerateDomainDetectsFile.c`](code/method.Intelix.Helper.Data.ConsolidatedFilesGenerator.GenerateDomainDetectsFile.c)
- [`code/method.Intelix.Helper.Data.ConsolidatedFilesGenerator.GenerateUserInformationFile.c`](code/method.Intelix.Helper.Data.ConsolidatedFilesGenerator.GenerateUserInformationFile.c)
- [`code/method.Intelix.Helper.Data.Counter.Collect.c`](code/method.Intelix.Helper.Data.Counter.Collect.c)
- [`code/method.Intelix.Helper.Data.Paths..cctor.c`](code/method.Intelix.Helper.Data.Paths..cctor.c)
- [`code/method.Intelix.Helper.Encrypted.Asn1Der.Parse.c`](code/method.Intelix.Helper.Encrypted.Asn1Der.Parse.c)
- [`code/method.Intelix.Helper.Encrypted.NssDumpMasterKey.Key3Database.c`](code/method.Intelix.Helper.Encrypted.NssDumpMasterKey.Key3Database.c)
- [`code/method.Intelix.Helper.Encrypted.NssDumpMasterKey.Key4Database.c`](code/method.Intelix.Helper.Encrypted.NssDumpMasterKey.Key4Database.c)
- [`code/method.Intelix.Helper.Sql.SqLite.ReadMasterTable.c`](code/method.Intelix.Helper.Sql.SqLite.ReadMasterTable.c)
- [`code/method.Intelix.Helper.Sql.SqLite.ReadTableFromOffset.c`](code/method.Intelix.Helper.Sql.SqLite.ReadTableFromOffset.c)
- [`code/method.Intelix.Targets.Applications.FTPRush.Collect.c`](code/method.Intelix.Targets.Applications.FTPRush.Collect.c)
- [`code/method.Intelix.Targets.Applications.RDCMan.Collect.c`](code/method.Intelix.Targets.Applications.RDCMan.Collect.c)
- [`code/method.Intelix.Targets.Applications.Rdp.Collect.c`](code/method.Intelix.Targets.Applications.Rdp.Collect.c)
- [`code/method.Intelix.Targets.Applications.Sunlogin.Collect.c`](code/method.Intelix.Targets.Applications.Sunlogin.Collect.c)
- [`code/method.Intelix.Targets.Browsers.Chromium.ProfileCollect.c`](code/method.Intelix.Targets.Browsers.Chromium.ProfileCollect.c)
- [`code/method.Intelix.Targets.Browsers.CryptoChromium..ctor.c`](code/method.Intelix.Targets.Browsers.CryptoChromium..ctor.c)
- [`code/method.Intelix.Targets.Crypto.CryptoDesktop..cctor.c`](code/method.Intelix.Targets.Crypto.CryptoDesktop..cctor.c)
- [`code/method.Intelix.Targets.Crypto.Grabber..ctor.c`](code/method.Intelix.Targets.Crypto.Grabber..ctor.c)
- [`code/method.Intelix.Targets.Device.ProcessDump.Collect.c`](code/method.Intelix.Targets.Device.ProcessDump.Collect.c)
- [`code/method.Intelix.Targets.Device.ScreenShot.Collect.c`](code/method.Intelix.Targets.Device.ScreenShot.Collect.c)
- [`code/method.Intelix.Targets.Device.WifiKey.TryExportAndParseProfiles.c`](code/method.Intelix.Targets.Device.WifiKey.TryExportAndParseProfiles.c)
- [`code/method.Intelix.Targets.Games.Minecraft.Collect.c`](code/method.Intelix.Targets.Games.Minecraft.Collect.c)
- [`code/method.Intelix.Targets.Games.Steam.Collect.c`](code/method.Intelix.Targets.Games.Steam.Collect.c)
- [`code/method._Main_d__5.MoveNext.c`](code/method._Main_d__5.MoveNext.c)
- [`code/method._SendToTelegram_d__6.MoveNext.c`](code/method._SendToTelegram_d__6.MoveNext.c)
- [`code/method.__c__DisplayClass18_0._YandexGetCard_b__0.c`](code/method.__c__DisplayClass18_0._YandexGetCard_b__0.c)
- [`code/sym.__c..cctor_17.c`](code/sym.__c..cctor_17.c)

## Behavioral Analysis

Based on the additional disassembly provided in chunk 2, here is the updated and extended technical analysis of the binary sample. All previous findings regarding its identity as an Information Stealer have been retained and integrated with the new evidence.

### Updated Technical Analysis

#### Core Functionality and Purpose
The binary remains confirmed as a sophisticated **Information Stealer (Infostealer)**. The additional disassembly confirms that the malware uses a modular approach to target a wide variety of credentials, expanding its reach beyond just web browsers to include server-side and remote access infrastructure.

*   **Expanded Data Harvesting:** 
    *   **Infrastructure Credentials:** The inclusion of `FTPRush` indicates a search for FTP (File Transfer Protocol) credentials, potentially aiming to gain access to web servers or storage systems.
    *   **Remote Access Tools:** The presence of `Rdp.Collect` suggests the malware targets Remote Desktop Protocol configurations. This is often used by attackers to find internal IP addresses and credentials to move laterally through a network or access remote servers.
    *   **Previous Targets (Retained):** Browser data (Chrome, Gecko), Financial information (Credit Cards, IBANs), Cryptocurrency wallets, and specific software like Steam, Sunlogin, and RDCMan.

#### Suspicious or Malicious Behaviors
The following behaviors are confirmed or further elaborated by the new code:

*   **Modular Collection Logic:** The naming convention `method.Intelix.Targets.Applications.[Name].Collect` suggests the malware is built on a modular framework. Each module handles a specific "target" type, allowing the attacker to easily add or remove data-harvesting capabilities (e.g., adding FTP or RDP modules).
*   **Data Exfiltration:** The reliance on Telegram for C2 communication (from chunk 1) remains the primary method for exfiltrating the diverse set of credentials identified in this and previous chunks.
*   **Anti-Analysis/Evasion:** The repeated presence of `halt_bad_data()` and "Bad instruction" warnings indicates that the malware employs significant **anti-disassembly techniques**. These are designed to break tools like Ghidra or IDA Pro, making it harder for researchers to statically analyze the full scope of the code.

#### Notable Techniques and Patterns
*   **Advanced Obfuscation & Junk Code:** 
    *   The disassembly shows highly complex, "messy" instructions (e.g., `CONCAT62`, `OVERLAPPING instruction`). This is a hallmark of **VM-based protection** or **heavy junk code insertion**. The goal is to confuse the disassembler's logic so that it cannot correctly identify where functions begin and end.
*   **Centralized Decryption Routine:** 
    *   The repetitive appearance of `method.CvMega.Helper.SimpleEncryptor.Decrypt` across different modules (Asn1Der, FTPRush, Rdp) indicates a unified decryption engine. The malware likely keeps its main configuration and several secondary "payload" strings encrypted, only decrypting them in memory during execution to evade static signature detection.
*   **Sophisticated Scripting/Framework Usage:**
    *   The naming conventions (e.g., `Intelix`, `CvMega`) suggest the use of a high-end **Malware-as-a-Service (MaaS)** framework. These frameworks are designed to be modular, allowing different "plug-ins" to target specific data types while sharing a common communication and decryption core.

---

### Updated Summary Table

| Feature | Observation | Risk Level |
| :--- | :--- | :--- |
| **Malware Type** | Information Stealer (Infostealer) | **High** |
| **Data Targets** | Passwords, Credit Cards, Crypto Wallets, Cookies, **FTP Credentials, RDP Configs** | **Critical** |
| **C2 Communication** | Telegram API / Bot Integration | **High** |
| **Obfuscation** | **Advanced:** Heavy junk code and overlapping instructions to thwart disassembly. | **High** |
| **Targeted Apps/Protocols** | Chrome, Firefox, Steam, Sunlogin, RDCMan, **FTP (FTPRush), Remote Desktop (Rdp)** | **High** |
| **Architecture** | Modular design; likely a commercial-grade "Malware-as-a-Service" framework. | **High** |

### Conclusion
The addition of the second chunk reinforces the severity of this threat. The malware is not just a simple script but a **highly organized, modular stealing tool**. It targets both personal data (passwords/crypto) and organizational infrastructure (FTP/RDP). Furthermore, its use of advanced anti-analysis techniques suggests it is designed to remain persistent and undetected by security researchers while automating the theft of high-value credentials.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1555.003 | Steal Web Browsing Information | The malware targets specific browser data (Chrome, Gecko) including passwords and cookies. |
| T1098 | Account Harvesting | The inclusion of "FTPRush" and "Rdp_Collect" indicates the theft of credentials for server access and lateral movement. |
| T1102 | Web Service | The malware uses a legitimate Telegram API/Bot integration to exfiltrate stolen data to its C2 infrastructure. |
| T1027 | Obfuscated Files or Programs | The use of junk code, overlapping instructions, and "bad" instruction markers is designed to hinder static analysis tools like Ghidra and IDA Pro. |
| T1027.002 | Packing | While the report mentions a decryption routine for payload strings, it indicates a layered approach to hide functionality from automated signature detection. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

### **IP addresses / URLs / Domains**
*   *None identified in the raw strings.*
*   **Note:** The behavior analysis identifies **Telegram** as the primary C2 (Command & Control) communication method for data exfiltration.

### **File paths / Registry keys**
*   `AppData` (referenced via `FindInAppData` - indicative of targeting user profile directories)
*   *Note: Specific browser profiles (Chrome, Firefox/Gecko) and system-level info (Hwid) are targeted through logic rather than hardcoded file paths in the provided strings.*

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
The following long hex strings were extracted from the data. Given their length (64 characters), these likely represent SHA-256 hashes used for integrity checks or, more likely, hardcoded cryptographic keys/seeds for the `SimpleEncryptor` module:
*   `2E69DC77B5DCFCCF57DD14F7E8BC6846C81B48D65C372C8970A25FA856421FE0`
*   `FA1AD270B23BA640E88EE7F51CC9C0C1A6C6BB1F2B9025682A7D30FB3BDA64F0`
*   `36CC5A112719A5E97DA145757C006C14F47D93716DBCC04E33DD5E931492C682`
*   `EE3D0135F2B5D54D61314A64157F43279B3E6088581A85C667D5686E3A675492`
*   `C2D8E5EED6CBEBD8625FC18F81486A7733C04F9B0129FFBE974C68B90308B4F2`

### **Other artifacts**
*   **C2 Patterns:** Telegram Bot API integration.
*   **Malware Frameworks/Modules:** 
    *   `Intelix` (Module identification)
    *   `CvMega` (Encryption/Utility library)
*   **Targeted Capabilities/Data Points:**
    *   `FTPRush` (FTP credential harvesting)
    *   `Rdp.Collect` (Remote Desktop configuration theft)
    *   `GetChromeWallets` / `GetGeckoWallets` (Crypto-wallet theft)
    *   `YandexGetCard` / `YandexPassword` (Yandex-specific data)
    *   `TokenRestore` (Session token harvesting)
    *   `GetHwid` (Hardware ID collection)
*   **Encryption Algorithms:** 
    *   `PBKDF2`
    *   `HMACSHA1`
*   **Anti-Analysis Techniques:** 
    *   Use of "junk code" and "overlapping instructions" to thwart disassemblers.
    *   Usage of a centralized decryption routine (`SimpleEncryptor.Decrypt`).

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: infostealer
3. **Confidence**: High
4. **Key evidence**:
    *   **Extensive Data Harvesting:** The malware targets a wide array of high-value data, including browser credentials (Chrome/Gecko), cryptocurrency wallets, and infrastructure access points (FTP and RDP configurations).
    *   **MaaS Framework Architecture:** The use of modular naming conventions (`Intelix`, `CvMega`) and a unified decryption routine indicates it is part of a professional "Malware-as-a-Service" framework rather than a simple standalone script.
    *   **Advanced Evasion Tactics:** The presence of junk code, overlapping instructions, and specialized obfuscation to thwart static analysis tools (Ghidra/IDA Pro) confirms its design for stealthy, persistent operation in production environments.
