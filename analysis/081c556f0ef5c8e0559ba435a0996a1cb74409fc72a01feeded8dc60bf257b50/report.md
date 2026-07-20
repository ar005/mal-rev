# Threat Analysis Report

**Generated:** 2026-07-18 01:51 UTC
**Sample:** `081c556f0ef5c8e0559ba435a0996a1cb74409fc72a01feeded8dc60bf257b50_081c556f0ef5c8e0559ba435a0996a1cb74409fc72a01feeded8dc60bf257b50.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `081c556f0ef5c8e0559ba435a0996a1cb74409fc72a01feeded8dc60bf257b50_081c556f0ef5c8e0559ba435a0996a1cb74409fc72a01feeded8dc60bf257b50.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, 4 sections |
| Size | 81,920 bytes |
| MD5 | `b0b80593525cec7f838273b1fdda6a52` |
| SHA1 | `38f9f68e51522255e63a26eca642428aa695a43a` |
| SHA256 | `081c556f0ef5c8e0559ba435a0996a1cb74409fc72a01feeded8dc60bf257b50` |
| Overall entropy | 6.646 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1767982509 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 49,152 | 6.279 | No |
| `.rdata` | 12,800 | 5.406 | No |
| `.data` | 16,896 | 6.964 | No |
| `.reloc` | 2,048 | 6.365 | No |

### Imports

**ntdll.dll**: `memset`, `RtlUnwind`, `_chkstk`
**KERNEL32.dll**: `IsBadReadPtr`, `GetACP`, `InterlockedDecrement`, `Sleep`, `GetProcAddress`, `GetLastError`, `HeapAlloc`, `ExitProcess`, `GetModuleHandleW`, `GlobalUnlock`, `GlobalLock`, `GlobalFree`, `GlobalAlloc`, `GetComputerNameA`, `WriteFile`
**USER32.dll**: `wsprintfA`

## Extracted Strings

Total strings found: **410** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
.reloc
Qh_p5:j
;Eu
Qhe$Xjj
u&j^9
t h|_K
E9Xt
^SSSSS
URPQQhp
Fh=xIK
v	N+D$
;t$,v-
kUQPXY]Y[
v4;5<OK
vL;5TOK
t"SS9] u
PPPPPPPP
PPPPPPPP
Content-Transfer-Encoding: binary
application/octet-stream
Content-Type: 
; filename="
Content-Disposition: form-data; name="
multipart/form-data; boundary=
application/x-www-form-urlencoded
chunked
Content-Range
Accept-Ranges
Location
Connection
Transfer-Encoding
Content-Length
Content-Type
User-Agent
Accept
Referer
HTTP/1.1
OPTIONS
CONNECT
UNLINK
DELETE
bytes=
0123456789ABCDEF

0


HTTP/1.
ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/
http://62.60.226.159/geter/index.php?
Mozilla/5.0
kernel32.dll
wininet.dll
status
winspool.drv
olE32.dll
psapi.dll
Imagehlp.dll
SHLWAPI.dll
crypt32.dll
gdiplus.dll
Gdi32.dll
opera.dll
cabinet.dll
winmm.dll
ssl3.dll
nspr4.dll
urlmon.dll
wininet.dll
shell32.dll
winsta.dll
ntdll.dll
ws2_32.dll
user32.dll
advapi32.dll
%s %d %s
Srv2003
Srv2003R2
Srv2008
Srv2008R2
%08X%08X
InstallDate
DigitalProductId
SOFTWARE\Microsoft\Windows NT\CurrentVersion
PROCESSOR_IDENTIFIER
IsWow64Process
</assembly>
	</trustInfo>
		</security>
			</requestedPrivileges>
				<requestedExecutionLevel level="requireAdministrator" uiAccess="false"></requestedExecutionLevel>
			<requestedPrivileges>
		<security>
	<trustInfo xmlns="urn:schemas-microsoft-com:asm.v3">
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0">
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
" /tr "
schtasks /create /sc minute /tn "
Global\%s
Online
1N39KVvVK8itaGr7odbrTKnBdbwt4n7PoY
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.004a5190` | `0x4a5190` | 3657 | ✓ |
| `fcn.004ac450` | `0x4ac450` | 887 | ✓ |
| `fcn.004a2a10` | `0x4a2a10` | 875 | ✓ |
| `fcn.004a7f80` | `0x4a7f80` | 798 | ✓ |
| `fcn.004a82a0` | `0x4a82a0` | 767 | ✓ |
| `fcn.004a95e0` | `0x4a95e0` | 701 | ✓ |
| `fcn.004a7c70` | `0x4a7c70` | 675 | ✓ |
| `fcn.004a45c0` | `0x4a45c0` | 658 | ✓ |
| `fcn.004a1930` | `0x4a1930` | 600 | ✓ |
| `fcn.004a38b0` | `0x4a38b0` | 587 | ✓ |
| `fcn.004a20d0` | `0x4a20d0` | 549 | ✓ |
| `fcn.004a23b0` | `0x4a23b0` | 548 | ✓ |
| `fcn.004ab9a9` | `0x4ab9a9` | 489 | ✓ |
| `fcn.004ac92e` | `0x4ac92e` | 487 | ✓ |
| `fcn.004a6e80` | `0x4a6e80` | 460 | ✓ |
| `fcn.004a1bf0` | `0x4a1bf0` | 443 | ✓ |
| `fcn.004a3ee0` | `0x4a3ee0` | 433 | ✓ |
| `fcn.004aa3d5` | `0x4aa3d5` | 431 | ✓ |
| `fcn.004a1db0` | `0x4a1db0` | 429 | ✓ |
| `fcn.004a4bb0` | `0x4a4bb0` | 422 | ✓ |
| `fcn.004aac31` | `0x4aac31` | 419 | ✓ |
| `fcn.004abb92` | `0x4abb92` | 410 | ✓ |
| `fcn.004ab672` | `0x4ab672` | 400 | ✓ |
| `fcn.004a6be0` | `0x4a6be0` | 397 | ✓ |
| `fcn.004a76e0` | `0x4a76e0` | 379 | ✓ |
| `fcn.004aaf3b` | `0x4aaf3b` | 364 | ✓ |
| `fcn.004a3bd0` | `0x4a3bd0` | 356 | ✓ |
| `fcn.004a1790` | `0x4a1790` | 338 | ✓ |
| `fcn.004a34e0` | `0x4a34e0` | 333 | ✓ |
| `fcn.004ab3ce` | `0x4ab3ce` | 331 | ✓ |

### Decompiled Code Files

- [`code/fcn.004a1790.c`](code/fcn.004a1790.c)
- [`code/fcn.004a1930.c`](code/fcn.004a1930.c)
- [`code/fcn.004a1bf0.c`](code/fcn.004a1bf0.c)
- [`code/fcn.004a1db0.c`](code/fcn.004a1db0.c)
- [`code/fcn.004a20d0.c`](code/fcn.004a20d0.c)
- [`code/fcn.004a23b0.c`](code/fcn.004a23b0.c)
- [`code/fcn.004a2a10.c`](code/fcn.004a2a10.c)
- [`code/fcn.004a34e0.c`](code/fcn.004a34e0.c)
- [`code/fcn.004a38b0.c`](code/fcn.004a38b0.c)
- [`code/fcn.004a3bd0.c`](code/fcn.004a3bd0.c)
- [`code/fcn.004a3ee0.c`](code/fcn.004a3ee0.c)
- [`code/fcn.004a45c0.c`](code/fcn.004a45c0.c)
- [`code/fcn.004a4bb0.c`](code/fcn.004a4bb0.c)
- [`code/fcn.004a5190.c`](code/fcn.004a5190.c)
- [`code/fcn.004a6be0.c`](code/fcn.004a6be0.c)
- [`code/fcn.004a6e80.c`](code/fcn.004a6e80.c)
- [`code/fcn.004a76e0.c`](code/fcn.004a76e0.c)
- [`code/fcn.004a7c70.c`](code/fcn.004a7c70.c)
- [`code/fcn.004a7f80.c`](code/fcn.004a7f80.c)
- [`code/fcn.004a82a0.c`](code/fcn.004a82a0.c)
- [`code/fcn.004a95e0.c`](code/fcn.004a95e0.c)
- [`code/fcn.004aa3d5.c`](code/fcn.004aa3d5.c)
- [`code/fcn.004aac31.c`](code/fcn.004aac31.c)
- [`code/fcn.004aaf3b.c`](code/fcn.004aaf3b.c)
- [`code/fcn.004ab3ce.c`](code/fcn.004ab3ce.c)
- [`code/fcn.004ab672.c`](code/fcn.004ab672.c)
- [`code/fcn.004ab9a9.c`](code/fcn.004ab9a9.c)
- [`code/fcn.004abb92.c`](code/fcn.004abb92.c)
- [`code/fcn.004ac450.c`](code/fcn.004ac450.c)
- [`code/fcn.004ac92e.c`](code/fcn.004ac92e.c)

## Behavioral Analysis

Based on the provided disassembly and strings, here is a technical analysis of the malware's behavior:

### Core Functionality and Purpose
The sample functions primarily as an **information stealer** and **spyware**. It is designed to identify its environment (anti-analysis), gather specific system information to create a unique identifier for the victim, and prepare data (including clipboard content) for exfiltration to a remote server.

### Suspicious or Malicious Behaviors

*   **Information Gathering & Fingerprinting:**
    *   The code heavily queries registry keys related to Windows versions (`Software\Microsoft\Windows NT\CurrentVersion`) and specific identifiers like `DigitalProductId` and `InstallDate`. This is used to fingerprint the machine.
    *   Function `fcn.004a7f80` specifically collects "computer names" and internal hardware/software IDs, likely to create a unique ID for the infected host.
*   **Clipboard Scraping:**
    *   The presence of `GetClipboardData`, `OpenClipboard`, and `SetClipboardData` in the strings suggests that the malware monitors or scrapes the system clipboard. This is commonly used by malware to steal passwords, crypto-wallet addresses, or private messages copied by the user.
*   **Command & Control (C2) Communication:**
    *   The strings include a hardcoded URL (`http://62.60.226.159/geter/index.php?`). The inclusion of headers like `User-Agent`, `Content-Type: application/octet-stream`, and the use of libraries like `wininet.dll` and `urlmon.dll` indicate it is designed to transmit stolen data via HTTP/HTTPS.
*   **Persistence Mechanism:**
    *   The string `schtasks /create /sc minute /tn` suggests the malware attempts to ensure its persistence by creating a scheduled task, ensuring it runs repeatedly (e.g., every minute) or on a regular interval.
*   **Anti-Analysis/Evasion:**
    *   The logic in `fcn.004a7c70` checks various OS versions (Vista, Server 2012, etc.). This is often used to detect if the code is running in a virtualized or sandboxed environment by checking for specific hardware strings or service behaviors.

### Notable Techniques and Patterns

*   **Obfuscated Data Processing:**
    *   Function `fcn.004a5190` shows an extensive series of arithmetic operations on large constants (e.g., `0x80604c15`, `0xfd469501`). This is a common technique for **de-obfuscating strings** or decrypting configuration blocks in memory to hide the true intent of the code from static analysis.
*   **Dynamic API Resolution:**
    *   The presence of `GetProcAddress` and `LoadLibraryA` suggests that the malware may resolve its primary malicious functions at runtime rather than listing them in the Import Address Table (IAT) to hinder automated detection.
*   **String Manipulation & Construction:**
    *   Several functions (like `fcn.004a6e80`) perform complex logic to build paths or internal strings on the fly, potentially to hide filenames or remote URLs from simple string searches during analysis.

### Summary of Evidence for Attribution/Categorization
The combination of **C2 communication**, **clipboard scraping**, and **automatic persistence** via `schtasks` strongly classifies this as a malicious "Infostealer" or "Trojans." The heavy use of obfuscation in the disassembly suggests it is designed to evade standard antivirus signatures.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1082** | System Information Discovery | The malware queries specific registry keys (e.g., `DigitalProductId`, `InstallDate`) to fingerprint the host and gather unique identifiers. |
| **T1539** | Steal Web Credentials | While not a direct "clipboard" technique, clipboard scraping is specifically utilized here to harvest sensitive data like passwords or credentials. |
| **T1071.001** | Application Layer Protocol: Web Protocols | The malware utilizes `wininet.dll` and hardcoded HTTP URLs to transmit gathered data to a remote server. |
| **T1053.005** | Scheduled Task | The use of the `schtasks` command confirms the creation of a scheduled task to ensure persistent execution on the system. |
| **T1497** | Virtualization/Sandbox Evasion | The logic checking for specific OS versions is a common tactic used to detect and bypass analysis environments like sandboxes or VMs. |
| **T1027** | Obfuscated Files or Information | The use of complex arithmetic operations to de-obfuscate strings at runtime is intended to hide malicious functionality from static analysis. |
| **T1106** | Native API | The use of `GetProcAddress` and `LoadLibraryA` indicates dynamic API resolution to bypass Import Address Table (IAT) scanning. |

---

## Indicators of Compromise

### INDICATORS OF COMPROMISE

**IP addresses / URLs / Domains**
*   **URL:** `http://62.60.226.159/geter/index.php?` (C2 communication)

**File paths / Registry keys**
*   *(None identified; "SOFTWARE\Microsoft\Windows NT\CurrentVersion" was excluded as a standard system path.)*

**Mutex names / Named pipes**
*   *(None found)*

**Hashes**
*   **MD5-style String:** `0x4382fd71bd5a4d921c27d851764d8c76ccc5d143` (Potentially a hardcoded identifier or file hash)

**Other artifacts**
*   **Persistence Mechanism:** Use of `schtasks /create /sc minute /tn` to establish execution every minute.
*   **Data Exfiltration Pattern:** Use of `Content-Type: application/octet-stream` and `User-Agent` headers for HTTP communication.
*   **Suspicious/Hardcoded Strings (Possible unique identifiers):** 
    *   `1N39KVvVK8itaGr7odbrTKnBdbwt4n7PoY`
    *   `LREe7WaYE2NUB9kgYce79AH4B79YbSPjJi`
    *   `TBWUnddB2J5cckALZenPo6KQJwLzysEohE`
*   **Behaviors:** 
    *   Clipboard scraping (via `GetClipboardData`, `OpenClipboard`, `SetClipboardData`).
    *   System fingerprinting via queries to `DigitalProductId` and `InstallDate`.
    *   Dynamic API resolution (`GetProcAddress`, `LoadLibraryA`) used to hide functionality from the IAT.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://62.60.226.159/geter/index.php?`

**IP addresses:**
- `62.60.226.159`

---

## Malware Family Classification

Based on the provided analysis, here is the classification of the sample:

1. **Malware family:** Unknown
2. **Malware type:** Infostealer
3. **Confidence:** High
4. **Key evidence:**
    *   **Data Theft & Collection:** The presence of clipboard scraping (via `GetClipboardData`) and system fingerprinting (registry queries for `DigitalProductId` and `InstallDate`) are primary indicators of an information stealer designed to harvest credentials and unique device identifiers.
    *   **Persistence & C2 Infrastructure:** The use of `schtasks` to ensure a recurring execution every minute, combined with a hardcoded IP address/URL (`62.60.226.159`) for exfiltration using standard web protocols, confirms its role as an automated data-harvesting tool.
    *   **Evasion Tactics:** The use of dynamic API resolution (`GetProcAddress`), string de-obfuscation (arithmetic on large constants), and OS version checking indicates a deliberate attempt to evade static analysis and sandbox detection.
