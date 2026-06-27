# Threat Analysis Report

**Generated:** 2026-06-27 06:52 UTC
**Sample:** `01be18e5bd3d04c79f8db21b72c06b84e724628e24f978a98aa86b4cb5b10499_01be18e5bd3d04c79f8db21b72c06b84e724628e24f978a98aa86b4cb5b10499.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `01be18e5bd3d04c79f8db21b72c06b84e724628e24f978a98aa86b4cb5b10499_01be18e5bd3d04c79f8db21b72c06b84e724628e24f978a98aa86b4cb5b10499.exe` |
| File type | PE32+ executable for MS Windows 5.02 (GUI), x86-64 (stripped to external PDB), 10 sections |
| Size | 274,768 bytes |
| MD5 | `2cd4e1d28f455756ffd8d3d05728cf3b` |
| SHA1 | `9b766cca40f5dd48da8e0552f3edd6003367c0fc` |
| SHA256 | `01be18e5bd3d04c79f8db21b72c06b84e724628e24f978a98aa86b4cb5b10499` |
| Overall entropy | 6.195 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1780873973 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 207,360 | 6.042 | No |
| `.data` | 4,096 | 0.611 | No |
| `.rdata` | 31,232 | 5.665 | No |
| `.pdata` | 5,120 | 5.062 | No |
| `.xdata` | 9,728 | 5.353 | No |
| `.bss` | 0 | 0.0 | No |
| `.idata` | 13,312 | 4.614 | No |
| `.tls` | 512 | -0.0 | No |
| `.rsrc` | 1,536 | 4.782 | No |
| `.reloc` | 512 | 4.11 | No |

### Imports

**ADVAPI32.dll**: `AdjustTokenPrivileges`, `AllocateAndInitializeSid`, `CheckTokenMembership`, `CloseServiceHandle`, `ControlService`, `CreateServiceA`, `DeleteService`, `DuplicateTokenEx`, `FreeSid`, `GetSidSubAuthority`, `GetSidSubAuthorityCount`, `GetTokenInformation`, `GetUserNameA`, `ImpersonateLoggedOnUser`, `ImpersonateNamedPipeClient`
**bcrypt.dll**: `BCryptCloseAlgorithmProvider`, `BCryptDecrypt`, `BCryptDestroyKey`, `BCryptEncrypt`, `BCryptGenRandom`, `BCryptGenerateSymmetricKey`, `BCryptOpenAlgorithmProvider`, `BCryptSetProperty`
**CRYPT32.dll**: `CryptUnprotectData`
**dbghelp.dll**: `MiniDumpWriteDump`
**DNSAPI.dll**: `DnsFree`
**GDI32.dll**: `BitBlt`, `CreateCompatibleBitmap`, `CreateCompatibleDC`, `DeleteDC`, `DeleteObject`, `GetDIBits`, `SelectObject`, `SetStretchBltMode`, `StretchBlt`
**IPHLPAPI.DLL**: `IcmpCloseHandle`, `IcmpCreateFile`, `IcmpSendEcho`
**KERNEL32.dll**: `CheckRemoteDebuggerPresent`, `CloseHandle`, `ConnectNamedPipe`, `CopyFileA`, `CreateDirectoryA`, `CreateFileA`, `CreateFileMappingA`, `CreateMutexA`, `CreateNamedPipeA`, `CreatePipe`, `CreateProcessA`, `CreateRemoteThread`, `CreateThread`, `CreateToolhelp32Snapshot`, `DeleteCriticalSection`
**api-ms-win-crt-convert-l1-1-0.dll**: `mbrtowc`, `strtol`, `strtoll`, `strtoul`, `strtoull`, `wcrtomb`
**api-ms-win-crt-environment-l1-1-0.dll**: `__p__environ`
**api-ms-win-crt-filesystem-l1-1-0.dll**: `_lock_file`, `_unlock_file`
**api-ms-win-crt-heap-l1-1-0.dll**: `_set_new_mode`, `calloc`, `free`, `malloc`, `realloc`
**api-ms-win-crt-locale-l1-1-0.dll**: `_configthreadlocale`, `localeconv`
**api-ms-win-crt-math-l1-1-0.dll**: `__setusermatherr`
**api-ms-win-crt-private-l1-1-0.dll**: `__C_specific_handler`, `memcmp`, `memcpy`, `memmove`, `strchr`, `strrchr`, `strstr`
**api-ms-win-crt-runtime-l1-1-0.dll**: `__p___argc`, `__p___argv`, `__p__acmdln`, `_cexit`, `_configure_narrow_argv`, `_crt_atexit`, `_errno`, `_exit`, `_initialize_narrow_environment`, `_set_app_type`, `_initterm`, `_initterm_e`, `_set_invalid_parameter_handler`, `abort`, `exit`
**api-ms-win-crt-stdio-l1-1-0.dll**: `__acrt_iob_func`, `__p__commode`, `__p__fmode`, `__stdio_common_vfprintf`, `__stdio_common_vsprintf_s`, `fclose`, `fopen`, `fputc`, `fputs`, `fread`, `fseek`, `ftell`, `fwrite`, `getc`, `rewind`
**api-ms-win-crt-string-l1-1-0.dll**: `_stricmp`, `isdigit`, `isspace`, `isxdigit`, `mbrlen`, `memset`, `strcmp`, `strlen`, `strncmp`, `strncpy`, `strnlen`, `strtok`, `tolower`, `wcslen`, `wcsnlen`
**api-ms-win-crt-utility-l1-1-0.dll**: `rand`, `srand`
**ole32.dll**: `CoCreateInstance`, `CoInitialize`, `CoInitializeEx`, `CoInitializeSecurity`, `CoSetProxyBlanket`, `CoUninitialize`

## Extracted Strings

Total strings found: **1717** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.data
.rdata
@.pdata
@.xdata
.idata
@.reloc
AWAVAUATUWVSH
X[^_]A\A]A^A_
8MZuEHcP<H
UAWAVAUATWVSH
[^_A\A]A^A_]
([^_]H
@' t	H
~D$8fH
@$A9@(~
AWAVAUATUWVSH
C$9C(~
H[^_]A\A]A^A_
S$9S(~
S$9S(~
UAWAVAUATWVSH
C$9C(~
C$9C(~
[^_A\A]A^A_]
UAWAVAUATWVSH
C$9C(~
C$9C(~
[^_A\A]A^A_]
UAVWVSH
C$9C(~
[^_A^]
[^_A^]
=UUUUw
S$9S(~
AUATUWVSH
X[^_]A\A]
AWAVAUATUWVSH
[^_]A\A]A^A_
u
9|$x
ATUWVSH
 [^_]A\
 [^_]A\
AWAVAUATUWVSH
[^_]A\A]A^A_
<'t4<IuhA
D$peE1
D$pB8D3
H9T$Pt
H9l$0L
L+L$`H
H9T$Pt
AWAVAUATUWVSH
8[^_]A\A]A^A_
AWAVAUATUWVSH
[^_]A\A]A^A_
[^_]A\A]A^A_
D$L)D$`
L$dL$L
T$8HcD$L;B
D|$0u

D$`+D$H
ATUWVSLcY
[^_]A\
[^_]A\
E9Y~!Ic
AWAVAUATUWVSH
8[^_]A\A]A^A_
AVAUATUWVSH
 [^_]A\A]A^
AUATUWVSH
([^_]A\A]
([^_]A\A]
WVSHcA
ATUWVSH
 [^_]A\
UWVSIc
E;A}"A
AUATUWVSH
H[^_]A\A]
AWAVAUATUWVSH
[^_]A\A]A^A_
\$`+l$H
D$P+D$X
AVAUATUWVSH
E;Yt&A
0[^_]A\A]A^
AWAVAUATUWVSH
8[^_]A\A]A^A_
AWAVAUATUWVSH
[^_]A\A]A^A_
AVAUATUWVSH
 [^_]A\A]A^
D$(+D$,
AWAVAUATUWVSH
|$`1u.H
[^_]A\A]A^A_
AWAVAUATUWVSH
[^_]A\A]A^A_
AWAVAUATUWVSH
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.140005dd0` | `0x140005dd0` | 187409 | ✓ |
| `fcn.1400338f0` | `0x1400338f0` | 141475 | ✓ |
| `fcn.140001420` | `0x140001420` | 64398 | ✓ |
| `fcn.140001d20` | `0x140001d20` | 62246 | ✓ |
| `fcn.14000d5e0` | `0x14000d5e0` | 8609 | ✓ |
| `fcn.140009dc0` | `0x140009dc0` | 7537 | ✓ |
| `fcn.14001cec0` | `0x14001cec0` | 5824 | ✓ |
| `fcn.140025980` | `0x140025980` | 4202 | ✓ |
| `fcn.14000f980` | `0x14000f980` | 3048 | ✓ |
| `fcn.140016bb0` | `0x140016bb0` | 2913 | ✓ |
| `fcn.140004e20` | `0x140004e20` | 2888 | ✓ |
| `fcn.14001e580` | `0x14001e580` | 2732 | ✓ |
| `fcn.140027a50` | `0x140027a50` | 2624 | ✓ |
| `fcn.14001a320` | `0x14001a320` | 2574 | ✓ |
| `fcn.140019a80` | `0x140019a80` | 2193 | ✓ |
| `fcn.14001c2d0` | `0x14001c2d0` | 2097 | ✓ |
| `fcn.140003770` | `0x140003770` | 2084 | ✓ |
| `fcn.14001f470` | `0x14001f470` | 1990 | ✓ |
| `fcn.14002c160` | `0x14002c160` | 1925 | ✓ |
| `fcn.140023c40` | `0x140023c40` | 1852 | ✓ |
| `fcn.14002a2a0` | `0x14002a2a0` | 1849 | ✓ |
| `fcn.14002c8f0` | `0x14002c8f0` | 1845 | ✓ |
| `fcn.140019360` | `0x140019360` | 1816 | ✓ |
| `fcn.14002a9e0` | `0x14002a9e0` | 1715 | ✓ |
| `fcn.140031290` | `0x140031290` | 1618 | ✓ |
| `fcn.140026ed0` | `0x140026ed0` | 1610 | ✓ |
| `fcn.14001b2e0` | `0x14001b2e0` | 1502 | ✓ |
| `fcn.140021190` | `0x140021190` | 1490 | ✓ |
| `fcn.14001b940` | `0x14001b940` | 1485 | ✓ |
| `fcn.140024c80` | `0x140024c80` | 1485 | ✓ |

### Decompiled Code Files

- [`code/fcn.140001420.c`](code/fcn.140001420.c)
- [`code/fcn.140001d20.c`](code/fcn.140001d20.c)
- [`code/fcn.140003770.c`](code/fcn.140003770.c)
- [`code/fcn.140004e20.c`](code/fcn.140004e20.c)
- [`code/fcn.140005dd0.c`](code/fcn.140005dd0.c)
- [`code/fcn.140009dc0.c`](code/fcn.140009dc0.c)
- [`code/fcn.14000d5e0.c`](code/fcn.14000d5e0.c)
- [`code/fcn.14000f980.c`](code/fcn.14000f980.c)
- [`code/fcn.140016bb0.c`](code/fcn.140016bb0.c)
- [`code/fcn.140019360.c`](code/fcn.140019360.c)
- [`code/fcn.140019a80.c`](code/fcn.140019a80.c)
- [`code/fcn.14001a320.c`](code/fcn.14001a320.c)
- [`code/fcn.14001b2e0.c`](code/fcn.14001b2e0.c)
- [`code/fcn.14001b940.c`](code/fcn.14001b940.c)
- [`code/fcn.14001c2d0.c`](code/fcn.14001c2d0.c)
- [`code/fcn.14001cec0.c`](code/fcn.14001cec0.c)
- [`code/fcn.14001e580.c`](code/fcn.14001e580.c)
- [`code/fcn.14001f470.c`](code/fcn.14001f470.c)
- [`code/fcn.140021190.c`](code/fcn.140021190.c)
- [`code/fcn.140023c40.c`](code/fcn.140023c40.c)
- [`code/fcn.140024c80.c`](code/fcn.140024c80.c)
- [`code/fcn.140025980.c`](code/fcn.140025980.c)
- [`code/fcn.140026ed0.c`](code/fcn.140026ed0.c)
- [`code/fcn.140027a50.c`](code/fcn.140027a50.c)
- [`code/fcn.14002a2a0.c`](code/fcn.14002a2a0.c)
- [`code/fcn.14002a9e0.c`](code/fcn.14002a9e0.c)
- [`code/fcn.14002c160.c`](code/fcn.14002c160.c)
- [`code/fcn.14002c8f0.c`](code/fcn.14002c8f0.c)
- [`code/fcn.140031290.c`](code/fcn.140031290.c)
- [`code/fcn.1400338f0.c`](code/fcn.1400338f0.c)

## Behavioral Analysis

This final chunk of disassembly provides the "smoking gun" evidence needed to finalize our profile of this malware. It confirms that the threat is not merely a trojan, but a **sophisticated multi-stage remote access trojan (RAT) and espionage tool** with professional-grade evasion, execution, and data theft capabilities.

### Final Analysis Update (Chunk 5/5)

#### 1. Reflection & Payload Execution (The "Loader" Logic)
Function `fcn.14002a2a0` is a high-complexity routine involving **Reflective Loading** and **Manual Mapping**.
*   **Process Injection:** The code utilizes `VirtualProtectEx`, `WriteProcessMemory`, and `CreateRemoteThread`. This confirms the malware injects its core logic into other processes to hide from Task Manager and basic security tools.
*   **In-Memory Assembly Execution:** Most strikingly, this function contains a **hardcoded x64 assembly block**. This is used to "bootstrap" a new stage of the attack. It manually resolves functions in memory (using `GetProcAddress` hidden behind an offset) and executes code that doesn't exist as a file on disk.
*   **Sophistication:** The use of "Reflective Loading" implies that the primary payload can be updated or swapped out, allowing the attacker to change capabilities without altering the initial dropper.

#### 2. Cryptography & Payload Decryption
Function `fcn.140019360` interacts with the **CNG (Cryptography Next Generation) API**.
*   **BCrypt Library:** The use of `BCryptOpenAlgorithmProvider`, `BCryptGenerateSymmetricKey`, and `BCryptDecrypt` indicates that the malware's configuration files, secondary payloads, or C2 communication packets are encrypted. 
*   **Why it matters:** This makes static analysis very difficult because most "malicious" strings (like IP addresses or commands) only appear in plain text for a fraction of a second while in memory after being decrypted by the `BCrypt` calls.

#### 3. Information Gathering & Stealing (The "Spyware" Component)
Function `fcn.140023c40` shows distinct evidence of data theft:
*   **Clipboard Scraping:** The call to `GetClipboardData` is used to steal information currently copied by the user (passwords, links, etc.).
*   **File Harvesting:** The code specifically scans for `.doc*` files in the `\Documents\` folders. This is a targeted search for corporate intelligence or personal documents.
*   **System Environment Mapping:** It uses `GetDiskFreeSpaceExA`, `GetTickCount`, and `GetSystemMetrics`. These are often used to "fingerprint" the machine, helping the attacker determine if they are inside a high-value target environment (e.g., identifying server hardware vs. a standard workstation).

#### 4. Advanced Networking & Interaction
Function `fcn.14002c160` reveals a complex approach to networking:
*   **Pseudo-Console Support:** The use of the `CreatePseudoConsole` family suggests the malware may be mimicking a serial port or a specific type of terminal interface to interact with system processes as if it were a legitimate administrative tool.
*   **Pipeline Management:** The logic involving "Pipes" and "Sockets" indicates that it is building a stable communication bridge, likely for an interactive remote shell (giving the attacker control over the command line).

#### 5. File System Manipulation & Persistence Logic
Function `fcn.140026ed0` shows advanced file management:
*   **Automatic Migration:** The code checks if it is running from a "suspicious" path (like a Temp folder) and attempts to move itself or its components to more permanent locations.
*   **File Verification:** It compares files against specific markers (like the `GLM1` identifier). This suggests it is checking for the presence of other modules or ensuring that only "valid" parts of its own code are executed after decryption.

---

### Final Technical Indicators for Incident Response:

| Feature | Observation | Threat Significance |
| :--- | :--- | :--- |
| **Reflective Loading** | `VirtualProtectEx`, `WriteProcessMemory`, `CreateRemoteThread` | **Critical**: Payload is injected into memory to bypass file-based scanners. |
| **Embedded Assembler** | Hardcoded x64 assembly "stage" launcher | **High**: Allows the malware to execute secondary stages without creating new files. |
| **Crypto Decryption** | `BCrypt` (CNG API) usage | **High**: Means C2 instructions and hidden features are encrypted on disk/in transit. |
| **Information Theft** | `GetClipboardData`, hunt for `.doc*` files | **Critical**: Directly indicates the intent to steal credentials and documents. |
| **Credential Harvesting**| `LogonUserW`, `ImpersonateLoggedOnUser` (from Chunk 4) | **High**: Used for lateral movement and privilege escalation. |
| **Evasion-Ware** | `KtmW32` (Transactional Files) & `CreatePseudoConsole` | **High**: Designed to hide from EDRs and masquerade as system tools. |

### Final Conclusion:
This is a **highly professional, multi-stage modular Trojan (likely part of an Advanced Persistent Threat - APT toolkit)**. 

It is designed for long-term residency on high-value systems. It doesn't just "infect" the computer; it **hides** within it using reflective loading and assembly stubs, **protects** its communications via the BCrypt library, and **executes specific theft tasks** (clipboard scraping and document searching) while actively seeking to elevate privileges through token manipulation and credential misuse. 

The complexity of this code—incorporating manufacturing-grade evasion techniques like Transactional File Systems and Reflective Loading—suggests it was developed by a sophisticated group rather than an automated "script kiddie" toolkit.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the observed behaviors from your analysis to the relevant MITRE ATT&CK techniques and sub-techniques below:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1055.001** | Process Injection | The use of `VirtualProtectEx`, `WriteProcessMemory`, and `CreateRemoteThread` confirms the injection of code into other processes to evade detection. |
| **T1613** | Dynamic Resolution | The inclusion of a hardcoded assembly block to resolve functions via `GetProcAddress` indicates an attempt to hide functionality from static analysis. |
| **T1562.001** | Data Encrypted | The utilization of the `BCrypt` (CNG) library suggests that configuration data, payloads, and communications are encrypted to hinder forensic investigation. |
| **T1083** | File and Directory Discovery | The specific search for `.doc*` files in common directories indicates a targeted effort to identify and harvest valuable information. |
| **T1113** | Gather User Info | The use of `GetTickCount`, `GetSystemMetrics`, and `GetDiskFreeSpaceExA` is used to fingerprint the environment and identify high-value targets. |
| **T1098** | Account Manipulation | The calls to `LogonUserW` and `ImpersonateLoggedOnUser` indicate attempts to manipulate credentials or gain higher privileges for lateral movement. |
| **T1036** | Masquerading | The use of `CreatePseudoConsole` is intended to make the malware appear as a legitimate system tool or administrative interface. |
| **T1574** | Hijack Execution Flow | The "Reflective Loading" logic allows the malware to execute code directly from memory, bypassing standard file-system monitoring. |

---

## Indicators of Compromise

As a threat intelligence analyst, I have analyzed the provided string data and behavioral reports. Below are the extracted Indicators of Compromise (IOCs) categorized by type. 

Note: The large block of repetitive alphanumeric strings at the beginning was analyzed; however, these appear to be obfuscated code fragments or "junk" data intended to hinder signature-based detection and do not contain distinct IP addresses, URLs, or unique file paths.

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   `\Documents\` (Targeted directory for `.doc*` file harvesting)
*   `cmd.exe` (Used for execution/command-line interaction)

### **Mutex names / Named pipes**
*   *None identified.* (The report mentions the "use of Pipes," but no specific named pipe strings were provided.)

### **Hashes**
*   *None identified.*

### **Other artifacts (Behavioral Signatures & Techniques)**
**Technical Indicators (API Calls/Functions):**
*   **Injection/Evasion:** `VirtualProtectEx`, `WriteProcessMemory`, `CreateRemoteThread` (Used for reflective loading and in-memory execution).
*   **Cryptography (CNG API):** `BCryptOpenAlgorithmProvider`, `BCryptGenerateSymmetricKey`, `BCryptDecrypt` (Used to encrypt C2 communications and payload components).
*   **Information Gathering:** `GetClipboardData` (Used for stealing copied credentials/data); `GetDiskFreeSpaceExA`, `GetTickCount`, `GetSystemMetrics` (Used for system fingerprinting).
*   **Credential Theft/Privilege Escalation:** `LogonUserW`, `ImpersonateLoggedOnUser`.

**Behavioral Artifacts:**
*   **Targeted File Types:** `.doc*` (Specific hunting for Office documents in user directories).
*   **Evasion Techniques:** Use of "Reflective Loading" to hide the primary payload and "Pseudo-Console" support to masquerade as a system tool.
*   **Internal Identifier:** `GLM1` (A specific identifier used by the malware to verify internal components/modules after decryption).
*   **Self-Migration Logic:** Automated check for "suspicious paths" (e.g., `%TEMP%` folders) and subsequent move to persistent locations.

---

## Malware Family Classification

Based on the analysis provided, here is the classification for the malware sample:

1. **Malware family:** Unknown (Potential APT Tool)
2. **Malware type:** RAT (Remote Access Trojan) / Spyware
3. **Confidence:** High
4. **Key evidence:**
    *   **Sophisticated Evasion & Injection:** The use of "Reflective Loading," manual mapping via x64 assembly stubs, and `CreateRemoteThread` confirms it is a sophisticated loader designed to execute payloads exclusively in memory to bypass signature-based detection.
    *   **Data Exfiltration/Spyware Capabilities:** Explicit functionality for clipboard scraping (`GetClipboardData`) and targeted harvesting of `.doc*` files indicates the primary goal is intellectual property theft and credential harvesting.
    *   **Advanced Persistence & Communication:** The implementation of `BCrypt` (CNG) encryption for C2 communication, "Pseudo-Console" masquerading, and automated self-migration from temporary folders points to a professional-grade tool intended for long-term residency on high-value targets.
