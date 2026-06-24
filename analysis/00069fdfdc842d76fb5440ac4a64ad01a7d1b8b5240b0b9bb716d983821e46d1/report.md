# Threat Analysis Report

**Generated:** 2026-06-23 15:46 UTC
**Sample:** `unpacked.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `unpacked.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 3 sections |
| Size | 109,056 bytes |
| MD5 | `7537fe40bc74718a5527521cc9ace81e` |
| SHA1 | `772e4b6dc64ba08ea5a666e442c881b7176fa3a6` |
| SHA256 | `00069fdfdc842d76fb5440ac4a64ad01a7d1b8b5240b0b9bb716d983821e46d1` |
| Overall entropy | 6.88 |
| Unpacked | ✓ Yes (tool: upx) |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1772912910 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 116,736 | 6.216 | No |
| `.rdata` | 104,448 | 7.101 | ⚠️ Yes |
| `.data` | 512 | 1.246 | No |
| `.pdata` | 2,560 | 4.706 | No |
| `.tls` | 512 | -0.0 | No |
| `.rsrc` | 1,536 | 4.46 | No |
| `.reloc` | 1,024 | 4.745 | No |

### Imports

**KERNEL32.DLL**: `CloseHandle`, `CompareFileTime`, `CopyFileW`, `CreateFileA`, `CreateFileW`, `CreateProcessA`, `CreateToolhelp32Snapshot`, `DeleteCriticalSection`, `DeleteFileA`, `DeleteFileW`, `EnterCriticalSection`, `ExitProcess`, `ExpandEnvironmentStringsW`, `FindClose`, `FindFirstFileW`
**ADVAPI32.dll**: `AdjustTokenPrivileges`, `CryptAcquireContextA`, `CryptAcquireContextW`, `CryptCreateHash`, `CryptDestroyHash`, `CryptGetHashParam`, `CryptHashData`, `CryptReleaseContext`, `DuplicateTokenEx`, `GetTokenInformation`, `GetUserNameA`, `ImpersonateLoggedOnUser`, `LookupPrivilegeValueW`, `OpenProcessToken`, `RegCloseKey`
**api-ms-win-crt-convert-l1-1-0.dll**: `strtod`
**api-ms-win-crt-environment-l1-1-0.dll**: `__p__environ`
**api-ms-win-crt-heap-l1-1-0.dll**: `_set_new_mode`, `calloc`, `free`, `malloc`, `realloc`
**api-ms-win-crt-locale-l1-1-0.dll**: `_configthreadlocale`
**api-ms-win-crt-math-l1-1-0.dll**: `__setusermatherr`
**api-ms-win-crt-private-l1-1-0.dll**: `__C_specific_handler`, `memchr`, `memcpy`, `memmove`, `strchr`, `strstr`, `wcschr`, `wcsrchr`, `wcsstr`
**api-ms-win-crt-runtime-l1-1-0.dll**: `__p___argc`, `__p___argv`, `_cexit`, `_configure_narrow_argv`, `_crt_atexit`, `_exit`, `_initialize_narrow_environment`, `_initterm`, `_initterm_e`, `_set_app_type`, `_set_invalid_parameter_handler`, `exit`, `signal`
**api-ms-win-crt-stdio-l1-1-0.dll**: `__acrt_iob_func`, `__p__commode`, `__p__fmode`, `__stdio_common_vfprintf`, `__stdio_common_vsprintf`, `__stdio_common_vsprintf_s`, `__stdio_common_vsscanf`, `__stdio_common_vswprintf`
**api-ms-win-crt-string-l1-1-0.dll**: `_strdup`, `_stricmp`, `_strnicmp`, `_wcsdup`, `_wcsicmp`, `_wcslwr`, `_wcsnicmp`, `isalnum`, `isspace`, `isxdigit`, `memset`, `strcat`, `strcmp`, `strcpy`, `strlen`
**api-ms-win-crt-time-l1-1-0.dll**: `_localtime64`, `_time64`, `strftime`
**api-ms-win-crt-utility-l1-1-0.dll**: `qsort`, `rand`, `srand`
**bcrypt.dll**: `BCryptCloseAlgorithmProvider`, `BCryptDecrypt`, `BCryptDestroyKey`, `BCryptGenerateSymmetricKey`, `BCryptOpenAlgorithmProvider`, `BCryptSetProperty`
**CRYPT32.dll**: `CryptStringToBinaryA`, `CryptUnprotectData`
**GDI32.dll**: `BitBlt`, `CreateCompatibleBitmap`, `CreateCompatibleDC`, `DeleteDC`, `DeleteObject`, `SelectObject`
**ncrypt.dll**: `NCryptDecrypt`, `NCryptFreeObject`, `NCryptOpenKey`, `NCryptOpenStorageProvider`
**ole32.dll**: `CoCreateGuid`, `CoCreateInstance`, `CoInitializeEx`, `CoInitializeSecurity`, `CoSetProxyBlanket`, `CoUninitialize`, `CreateStreamOnHGlobal`
**OLEAUT32.dll**: `SysAllocString`, `SysFreeString`, `VariantClear`, `VariantInit`
**SHELL32.dll**: `SHGetFolderPathW`

## Extracted Strings

Total strings found: **1375** (showing first 100)

```
!This program cannot be run in DOS mode.$
`.rdata
@.data
.pdata
@.reloc
AWAVAUATVWUSH
fffff.
9MZu<HcQ<
8[]_^A\A]A^A_
UAWAVAUATVWSH
fffff.
Unknown
ffffff.
[_^A\A]A^A_]
([]_^H
([]_^H
AWAVAUATVWUSH
fffff.
([]_^A\A]A^A_
([]_^A\A]A^A_H
AWAVAUATVWUSH
[]_^A\A]A^A_
fffff.
AWAVAUATVWUSH
[]_^A\A]A^A_
AWAVAUATVWUSH
ffffff.
)t$ I)
[]_^A\A]A^A_
AVVWUSH
 []_^A^H
 []_^A^
HcFxH9
AWAVATVWUSH
 []_^A\A^A_H
 []_^A\A^A_
AWAVAUATVWUSH
h[]_^A\A]A^A_
h[]_^A\A]A^A_H
AWAVATVWSH
[_^A\A^A_
AVVWSH
([_^A^
([_^A^
AVVWSH
ffffff.
([_^A^
AVVWSH
H9|$(t
H
8[_^A^
AWAVAUATVWUSH
[]_^A\A]A^A_
[]_^A\A]A^A_
fffff.
AWAVAUATVWUSH
([]_^A\A]A^A_
fffff.
ffffff.
fffff.
AWAVAUATVWUSH
[]_^A\A]A^A_
AWAVAUATVWUSH
([]_^A\A]A^A_
([]_^A\A]A^A_H
AWAVAUATVWUSH
[]_^A\A]A^A_
AWAVAUATVWUSH
 DPE	
D$,Icv
fffff.
ffffff.
fffff.
fffff.
fffff.
D$ v*M
D$0HcH
fffff.
ffffff.
[]_^A\A]A^A_
fffff.
AWAVATVWUSH
0[]_^A\A^A_
AWAVAUATVWSH
 [_^A\A]A^A_
AWAVAUATVWUSH
fffff.
D$Ht)H
[]_^A\A]A^A_
AWAVAUATVWUSH
l$8t*f
[]_^A\A]A^A_
AWAVAUATVWUSH
[]_^A\A]A^A_
AWAVVWSH
[_^A^A_
AWAVAUATVWUSH
ffffff.
[]_^A\A]A^A_
AVVWSH
H[_^A^
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.14001c9b0` | `0x14001c9b0` | 114822 | ✓ |
| `fcn.14001a7b0` | `0x14001a7b0` | 5025 | ✓ |
| `fcn.140004c80` | `0x140004c80` | 4046 | ✓ |
| `fcn.140003800` | `0x140003800` | 3249 | ✓ |
| `fcn.14000c220` | `0x14000c220` | 3160 | ✓ |
| `fcn.140015ef0` | `0x140015ef0` | 2875 | ✓ |
| `fcn.14001cbf0` | `0x14001cbf0` | 2806 | ✓ |
| `fcn.140010050` | `0x140010050` | 2774 | ✓ |
| `entry1` | `0x14001c850` | 2578 | ✓ |
| `fcn.14000a960` | `0x14000a960` | 2483 | ✓ |
| `fcn.140007e20` | `0x140007e20` | 2150 | ✓ |
| `fcn.14000a190` | `0x14000a190` | 1990 | ✓ |
| `fcn.140007690` | `0x140007690` | 1889 | ✓ |
| `fcn.140001bd0` | `0x140001bd0` | 1585 | ✓ |
| `fcn.14001c000` | `0x14001c000` | 1367 | ✓ |
| `fcn.140007880` | `0x140007880` | 1202 | ✓ |
| `fcn.14001bb60` | `0x14001bb60` | 1183 | ✓ |
| `fcn.140002e80` | `0x140002e80` | 1168 | ✓ |
| `fcn.14000eda0` | `0x14000eda0` | 1141 | ✓ |
| `fcn.140011c20` | `0x140011c20` | 1126 | ✓ |
| `fcn.14000e540` | `0x14000e540` | 983 | ✓ |
| `fcn.1400013e0` | `0x1400013e0` | 942 | ✓ |
| `fcn.1400063a0` | `0x1400063a0` | 942 | ✓ |
| `fcn.140002500` | `0x140002500` | 923 | ✓ |
| `fcn.140001020` | `0x140001020` | 891 | ✓ |
| `fcn.140005c50` | `0x140005c50` | 884 | ✓ |
| `fcn.1400128b0` | `0x1400128b0` | 845 | ✓ |
| `fcn.140004950` | `0x140004950` | 812 | ✓ |
| `fcn.140006840` | `0x140006840` | 760 | ✓ |
| `fcn.140002210` | `0x140002210` | 744 | ✓ |

### Decompiled Code Files

- [`code/entry1.c`](code/entry1.c)
- [`code/fcn.140001020.c`](code/fcn.140001020.c)
- [`code/fcn.1400013e0.c`](code/fcn.1400013e0.c)
- [`code/fcn.140001bd0.c`](code/fcn.140001bd0.c)
- [`code/fcn.140002210.c`](code/fcn.140002210.c)
- [`code/fcn.140002500.c`](code/fcn.140002500.c)
- [`code/fcn.140002e80.c`](code/fcn.140002e80.c)
- [`code/fcn.140003800.c`](code/fcn.140003800.c)
- [`code/fcn.140004950.c`](code/fcn.140004950.c)
- [`code/fcn.140004c80.c`](code/fcn.140004c80.c)
- [`code/fcn.140005c50.c`](code/fcn.140005c50.c)
- [`code/fcn.1400063a0.c`](code/fcn.1400063a0.c)
- [`code/fcn.140006840.c`](code/fcn.140006840.c)
- [`code/fcn.140007690.c`](code/fcn.140007690.c)
- [`code/fcn.140007880.c`](code/fcn.140007880.c)
- [`code/fcn.140007e20.c`](code/fcn.140007e20.c)
- [`code/fcn.14000a190.c`](code/fcn.14000a190.c)
- [`code/fcn.14000a960.c`](code/fcn.14000a960.c)
- [`code/fcn.14000c220.c`](code/fcn.14000c220.c)
- [`code/fcn.14000e540.c`](code/fcn.14000e540.c)
- [`code/fcn.14000eda0.c`](code/fcn.14000eda0.c)
- [`code/fcn.140010050.c`](code/fcn.140010050.c)
- [`code/fcn.140011c20.c`](code/fcn.140011c20.c)
- [`code/fcn.1400128b0.c`](code/fcn.1400128b0.c)
- [`code/fcn.140015ef0.c`](code/fcn.140015ef0.c)
- [`code/fcn.14001a7b0.c`](code/fcn.14001a7b0.c)
- [`code/fcn.14001bb60.c`](code/fcn.14001bb60.c)
- [`code/fcn.14001c000.c`](code/fcn.14001c000.c)
- [`code/fcn.14001c9b0.c`](code/fcn.14001c9b0.c)
- [`code/fcn.14001cbf0.c`](code/fcn.14001cbf0.c)

## Behavioral Analysis

This updated analysis incorporates the final chunk of disassembly. The addition of these functions confirms that while the malware has a strong focus on Mozilla Firefox, it is actually a **multi-vector information stealer** designed to harvest credentials from several high-value targets including **Telegram**, **Chrome/Chromium-based browsers**, and potentially other local system artifacts.

### Updated Summary
The final disassembly reveals a significant expansion of the malware’s scope. It moves beyond just Firefox's `ns3.dll` to include:
1.  **Cross-Browser Targeting:** It implements logic common in "RedLine" or "Vidar" style stealers that target Chromium-based browsers by looking for `Local State` files and specifically searching for the `"app_bound_encrypted_key"`—a key used by Chrome to protect data from non-system processes.
2.  **Instant Messaging Targeting:** It contains specific logic to detect and extract data from **Telegram**, identifying multiple versions of the application (e.g., Telegram 1 through 5).
3.  **Advanced Cryptographic Processing:** The inclusion of a custom implementation of a stream cipher (likely **ChaCha20** or **Salsa20**) indicates that once it finds "encrypted" data from these applications, it has the internal logic to decrypt it before exfiltration.

---

### New Findings from Chunk 3

#### 1. Multi-Target Expansion (Telegram & Chromium)
*   **Function `fcn.14000e540`:** This function is a clear indicator of multi-target support. It specifically looks for "Steam" and then checks for various **Telegram** configurations. The logic to search for `"app_bound_encrypted_key"` followed by a decryption routine suggests it targets the encryption layer used by Chromium and modern messaging apps to protect local databases.
*   **Function `fcn.140006840`:** This function iterates through the `C:\Users` directory to identify valid user profiles (excluding "Public" and system accounts). It then maps these paths to specific system files, likely looking for authentication tokens or cookies stored in standard local app data directories.

#### 2. Advanced Decryption & Cryptography
*   **Function `fcn.140002210`:** This is a high-complexity mathematical loop consisting of bitwise rotations (e.g., `>> 0x10`, `<< 0xc`), XOR operations, and additions in a structured block pattern. This is characteristic of **ChaCha20** or **Salsa20** stream ciphers. The malware uses this to process raw data that it has extracted from the target applications' local storage files.
*   **NCrypt API Usage:** In `fcn.14000eda0`, the malware uses the Windows **CNCRYPT** library (`NCryptOpenStorageProvider`, `NCryptOpenKey`) to decrypt values stored via DPAPI (Data Protection API). This is a common technique used by advanced stealers to bypass Windows' native protection on cookies and passwords.

#### 3. Persistence of Identification
*   **Function `fcn.1400063a0`:** This function performs extensive "cleaning" and validation of file paths, ensuring it identifies the correct directories even if they are hidden or nested within standard system folders (e.g., checking for `systemprofile` to avoid grabbing system-level accounts).

---

### Updated Summary of Findings

| Feature | Observation | Risk Level |
| :--- | :--- | :--- |
| **Cross-Platform Stealing** | Targets Firefox, Telegram, and Chromium-based browsers (via "app_bound" keys). | **Critical** |
| **Advanced Cryptography** | Implements custom ChaCha20/Salsa20 logic to decrypt local data post-extraction. | **High** |
| **DPAPI Bypassing** | Uses `NCrypt` APIs to decrypt system-protected credentials. | **High** |
| **User Profiling** | Iterates through all user profiles in `C:\Users` to find as many targets as possible. | **High** |
| **Data Exfiltration** | Uses WinHttp with multi-part/zip structures (from previous analysis). | **High** |
| **Anti-Forensics** | Stages files in Temp and deletes them; uses complex path cleaning logic. | **Medium** |

### Conclusion of Analysis
The final disassembly confirms that the binary is a **sophisticated, multi-target information stealer.** It is not merely looking for Firefox passwords; it is designed to harvest credentials from any high-value local application that uses standard encryption methods (like DPAPI or ChaCha20) to protect its data. 

By targeting **Firefox**, **Telegram**, and **Chromium** browsers simultaneously, the malware maximizes its "payout" per infection. The presence of professional-grade decryption routines and systematic user-profile enumeration classifies this as a high-capability piece of malware likely associated with organized cybercrime groups.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1539** | Steal Web Credentials | The malware specifically targets and extracts credentials from Firefox, Chrome, and Chromium-based browsers. |
| **T1083** | File and Directory Discovery | The malware iterates through the `C:\Users` directory to identify system files and local application data for harvesting. |
| **T1555.003** | Web Browsers | The analysis notes specific targeting of browser artifacts like `ns3.dll` and `Local State` files. |
| **T1486** | Data Manipulation Indicator | The inclusion of custom ChaCha20/Salsa20 logic is used to decrypt data extracted from local storage before exfiltration. |
| **T1560** | Archive Collected Data | The use of multi-part and zip structures indicates that the malware packages gathered data for efficient transport. |
| **T1041** | Exfiltrate Data | The use of WinHttp to transmit the collected information from the local system to a remote server. |
| **T1070.004** | Indicator Removal on Host: File Deletion | The malware stages files in the Temp directory and deletes them to evade detection and forensic analysis. |
| **T1112** | Modify Certificate/Key Storage | The use of `NCrypt` libraries to bypass DPAPI indicates an attempt to access protected system keys. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Please note that the **Strings** section contains significant amounts of obfuscated data or "junk" code (e.g., `AWAVAUATVWUSH`, `fffff.`); therefore, no direct IP addresses or file hashes were identified in that specific block. The primary intelligence is derived from the **Behavioral Analysis**.

### **IP addresses / URLs / Domains**
*   *(None identified)*
    *   *Note: While "WinHttp" is mentioned as a protocol for exfiltration, no specific C2 (Command & Control) domains or IP addresses were provided in the source text.*

### **File paths / Registry keys**
*   **Local State** (Targeted file used by Chromium-based browsers to store encryption keys)
*   **"app_bound_encrypted_key"** (Specific key/identifier targeted within the `Local State` file to bypass Chrome's protection)
*   **C:\Users\** (System path iterated by the malware to locate user profiles; however, this is a common system path and utilized as a scanning behavior).

### **Mutex names / Named pipes**
*   *(None identified)*

### **Hashes**
*   *(None provided in the source text)*

### **Other artifacts (Behavioral IOCs)**
*   **Targeted Applications:** 
    *   Mozilla Firefox (specifically targeting `ns3.dll`)
    *   Telegram (identifying versions 1 through 5)
    *   Chromium-based browsers (Google Chrome, Microsoft Edge, etc.)
*   **Cryptographic Signatures:**
    *   Custom implementation of **ChaCha20** or **Salsa20** stream ciphers (used for decrypting stolen data).
    *   Use of Windows **NCrypt API** (`NCryptOpenStorageProvider`, `NCryptOpenKey`) to bypass DPAPI protections on system-protected credentials.
*   **Exfiltration Patterns:**
    *   Use of **WinHttp** for exfiltration.
    *   Utilization of **multi-part/zip structures** during the data exfiltration phase.
*   **Anti-Forensics/Evasion:**
    *   Staging files in `Temp` directories followed by immediate deletion after exfiltration.
    *   Advanced path cleaning logic to identify hidden or nested folders within user profiles.

---

## Malware Family Classification

1. **Malware family**: Information Stealer (Behaviorally similar to RedLine or Vidar)
2. **Malware type**: infostealer
3. **Confidence**: High
4. **Key evidence**:
    *   **Multi-Target Harvesting:** The malware systematically targets high-value credentials from multiple platforms, specifically Firefox (`ns3.dll`), Telegram (versions 1-5), and Chromium-based browsers by targeting `Local State` files and "app_bound" keys.
    *   **Advanced Cryptographic Decryption:** It employs sophisticated techniques to bypass security measures, including the use of **NCrypt APIs** to circumvent DPAPI and a custom implementation of **ChaCha20/Salsa20** stream ciphers to decrypt stolen data before exfiltration.
    *   **Sophisticated Exfiltration & Evasion:** The malware uses **WinHttp** for multi-part/zip data transport and employs anti-forensic techniques, such as staging files in the `Temp` directory and deleting them immediately after transmission.
