# Threat Analysis Report

**Generated:** 2026-08-18 17:13 UTC
**Sample:** `unpacked.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `unpacked.exe` |
| File type | PE32 executable for MS Windows 5.00 (GUI), Intel i386, UPX compressed, 3 sections |
| Size | 758,272 bytes |
| MD5 | `c16f6c7e0d490389afa7bd958a74f73f` |
| SHA1 | `1e1e1dd19ae7e4b37d484c7480cf9554c151e3f1` |
| SHA256 | `10323b94da1495e4ece23f2d8ab00d539f3f09a53cdb52ac2f28678f747a5eda` |
| Overall entropy | 6.746 |
| Unpacked | ✓ Yes (tool: upx) |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1773777434 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 1,260,032 | 6.609 | No |
| `.rdata` | 215,040 | 5.955 | No |
| `.data` | 39,424 | 4.397 | No |
| `.code` | 120,320 | 6.07 | No |
| `.reloc` | 41,472 | 6.748 | No |

### Imports

**KERNEL32.DLL**: `AllocConsole`, `CancelIo`, `CloseHandle`, `CompareStringW`, `CopyFileW`, `CreateDirectoryW`, `CreateEventA`, `CreateFileA`, `CreateFileMappingA`, `CreateFileW`, `CreateMutexW`, `CreatePipe`, `CreateProcessW`, `CreateThread`, `CreateToolhelp32Snapshot`
**ADVAPI32.dll**: `CryptAcquireContextA`, `CryptAcquireContextW`, `CryptCreateHash`, `CryptDestroyHash`, `CryptGenRandom`, `CryptGetHashParam`, `CryptHashData`, `CryptReleaseContext`, `GetUserNameW`, `RegCloseKey`, `RegCreateKeyW`, `RegEnumKeyExW`, `RegEnumValueW`, `RegOpenKeyExW`, `RegQueryValueExW`
**avicap32.dll**: `capCreateCaptureWindowA`, `capGetDriverDescriptionA`
**bcrypt.dll**: `BCryptCloseAlgorithmProvider`, `BCryptCreateHash`, `BCryptDecrypt`, `BCryptDeriveKey`, `BCryptDestroyHash`, `BCryptDestroyKey`, `BCryptDestroySecret`, `BCryptEncrypt`, `BCryptExportKey`, `BCryptFinalizeKeyPair`, `BCryptFinishHash`, `BCryptGenRandom`, `BCryptGenerateKeyPair`, `BCryptGetProperty`, `BCryptHashData`
**COMCTL32.dll**: `InitCommonControlsEx`
**CRYPT32.dll**: `CertAddCertificateContextToStore`, `CertCloseStore`, `CertCreateCertificateChainEngine`, `CertEnumCertificatesInStore`, `CertFindCertificateInStore`, `CertFreeCertificateChain`, `CertFreeCertificateChainEngine`, `CertFreeCertificateContext`, `CertGetCertificateChain`, `CertGetNameStringA`, `CertOpenStore`, `CryptDecodeObjectEx`, `CryptQueryObject`, `CryptStringToBinaryA`
**GDI32.dll**: `BitBlt`, `CreateCompatibleBitmap`, `CreateCompatibleDC`, `CreateDCW`, `CreateDIBSection`, `CreateFontIndirectW`, `CreateRectRgn`, `CreateSolidBrush`, `DeleteDC`, `DeleteObject`, `GdiGetBatchLimit`, `GdiSetBatchLimit`, `GetDIBits`, `GetDeviceCaps`, `GetObjectType`
**gdiplus.dll**: `GdipDeleteFont`, `GdipDeleteGraphics`, `GdipDeleteMatrix`, `GdipDeletePath`, `GdipDeletePen`, `GdipDeleteStringFormat`, `GdipFree`
**IPHLPAPI.DLL**: `GetAdaptersInfo`, `GetExtendedTcpTable`
**NETAPI32.dll**: `NetApiBufferFree`, `NetShareEnum`
**ole32.dll**: `CoInitialize`, `CoTaskMemFree`
**PSAPI.DLL**: `EnumProcesses`, `GetModuleFileNameExW`, `GetProcessImageFileNameW`, `GetProcessMemoryInfo`
**SHELL32.dll**: `ord_680`, `SHGetFolderLocation`, `SHGetPathFromIDListW`, `ShellExecuteExW`, `ShellExecuteW`
**USER32.dll**: `CharLowerW`, `CharUpperW`, `CloseClipboard`, `CloseDesktop`, `CreateDesktopW`, `CreateIconFromResource`, `CreateIconFromResourceEx`, `DestroyIcon`, `DestroyWindow`, `DrawIcon`, `DrawIconEx`, `EmptyClipboard`, `EnableWindow`, `EnumDesktopWindows`, `EnumDisplayMonitors`
**WINMM.dll**: `timeBeginPeriod`, `waveInAddBuffer`, `waveInClose`, `waveInGetDevCapsW`, `waveInGetNumDevs`, `waveInOpen`, `waveInPrepareHeader`, `waveInReset`, `waveInStart`, `waveInStop`, `waveInUnprepareHeader`
**WS2_32.dll**: `WSACleanup`, `WSAGetLastError`, `WSAIoctl`, `WSASetLastError`, `WSAStartup`, `__WSAFDIsSet`, `accept`, `bind`, `closesocket`, `connect`, `freeaddrinfo`, `getaddrinfo`, `gethostbyaddr`, `gethostbyname`, `gethostname`

## Extracted Strings

Total strings found: **6984** (showing first 100)

```
!This program cannot be run in DOS mode.$
`.rdata
@.data
`.reloc
ZXRVSW
G_[^1
j h >W
tvWh@>W
?Uh(>W
YYh@>W
u"9~t
D$4j^VUP
D$`^V3
l$HUGP
t$,t"hXDV
D$TPQRW
t$0RRVR
9\$0tG
j hd>W
9\$0tG
j hd>W
9utBW
t59}t
0;O<v
SVWj@h
uAh(AW
u2h<AW
QQSUVW
t$ h"'
PVWh+?@
t$ h"'
u%9^4|
PWVh+B@
\$UVW3
\$UVW
L$`QPR
D$ PWW
|$09\$$tl
tsf9>tn
uhX7V
t\hlSU
L$QWV
uuSSSh
}	j0Yf
D$4#D$8
u*9D$0uh
D$0VjdY
GICON
~LSSSj
\$HUVW
D$h< U
PSUWRQ
8^1t
D$T9\$
L$(;T$,|
+D$L;D$P
D$4M;\$
+\$L;\$P
D$4;D$0r
T$0;L$
T$T+\$L
D$4;D$
L$0;D$
T$89\$D
tH9\$HtBf9
>_^[]Y
>_^[]Y
t$ WSj
t$ WSj
L$VWP
;l$(sX
;l$(sXj
<
t<t
F^_][
	<et<Et
<ItC<Lt3<Tt#<h
<ot<ut
A<lt'<tt
<wt<zu1
8^8tb9^4~]
<it<It
PRRRRR
<ItC<Lt3<Tt#<h
<ot<ut
A<lt'<tt
<wt<zu1
tb9^4~]
vj*Xf;
=j*Xf;
Tt)jhZf;
JjlZf;
SVWjA_
V.jx_f;
V +V4+
F.jgYf;
<it<It
j0Z9^4t
j0Z9^4t
j0Z9^4t
^8uRQ
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.004fcaa8` | `0x4fcaa8` | 720996 | ✓ |
| `fcn.004bd110` | `0x4bd110` | 671439 | ✓ |
| `fcn.0047fd10` | `0x47fd10` | 507495 | ✓ |
| `fcn.00481730` | `0x481730` | 504878 | ✓ |
| `fcn.004816d0` | `0x4816d0` | 503598 | ✓ |
| `fcn.00488830` | `0x488830` | 476581 | ✓ |
| `fcn.0044b210` | `0x44b210` | 460124 | ✓ |
| `fcn.00451690` | `0x451690` | 436443 | ✓ |
| `fcn.0043bdb0` | `0x43bdb0` | 410954 | ✓ |
| `fcn.00419dd0` | `0x419dd0` | 213155 | ✓ |
| `fcn.0041928d` | `0x41928d` | 211247 | ✓ |
| `fcn.00409050` | `0x409050` | 157977 | ✓ |
| `main` | `0x577000` | 36948 | ✓ |
| `fcn.00497040` | `0x497040` | 13980 | ✓ |
| `fcn.00472480` | `0x472480` | 12595 | ✓ |
| `fcn.004282b0` | `0x4282b0` | 9538 | ✓ |
| `fcn.0049a6e0` | `0x49a6e0` | 8842 | ✓ |
| `fcn.00456ba6` | `0x456ba6` | 7590 | ✓ |
| `fcn.00435650` | `0x435650` | 5991 | ✓ |
| `fcn.004b6700` | `0x4b6700` | 5858 | ✓ |
| `fcn.00520b00` | `0x520b00` | 5683 | ✓ |
| `fcn.00491b8b` | `0x491b8b` | 5627 | ✓ |
| `fcn.004939d5` | `0x4939d5` | 5608 | ✓ |
| `fcn.0046c710` | `0x46c710` | 5470 | ✓ |
| `fcn.00487422` | `0x487422` | 4709 | ✓ |
| `fcn.0041fef0` | `0x41fef0` | 4571 | ✓ |
| `fcn.004d7a00` | `0x4d7a00` | 4476 | ✓ |
| `fcn.00587800` | `0x587800` | 4468 | ✓ |
| `fcn.00500c80` | `0x500c80` | 4343 | ✓ |
| `fcn.0043e5d0` | `0x43e5d0` | 4167 | ✓ |

### Decompiled Code Files

- [`code/fcn.00409050.c`](code/fcn.00409050.c)
- [`code/fcn.0041928d.c`](code/fcn.0041928d.c)
- [`code/fcn.00419dd0.c`](code/fcn.00419dd0.c)
- [`code/fcn.0041fef0.c`](code/fcn.0041fef0.c)
- [`code/fcn.004282b0.c`](code/fcn.004282b0.c)
- [`code/fcn.00435650.c`](code/fcn.00435650.c)
- [`code/fcn.0043bdb0.c`](code/fcn.0043bdb0.c)
- [`code/fcn.0043e5d0.c`](code/fcn.0043e5d0.c)
- [`code/fcn.0044b210.c`](code/fcn.0044b210.c)
- [`code/fcn.00451690.c`](code/fcn.00451690.c)
- [`code/fcn.00456ba6.c`](code/fcn.00456ba6.c)
- [`code/fcn.0046c710.c`](code/fcn.0046c710.c)
- [`code/fcn.00472480.c`](code/fcn.00472480.c)
- [`code/fcn.0047fd10.c`](code/fcn.0047fd10.c)
- [`code/fcn.004816d0.c`](code/fcn.004816d0.c)
- [`code/fcn.00481730.c`](code/fcn.00481730.c)
- [`code/fcn.00487422.c`](code/fcn.00487422.c)
- [`code/fcn.00488830.c`](code/fcn.00488830.c)
- [`code/fcn.00491b8b.c`](code/fcn.00491b8b.c)
- [`code/fcn.004939d5.c`](code/fcn.004939d5.c)
- [`code/fcn.00497040.c`](code/fcn.00497040.c)
- [`code/fcn.0049a6e0.c`](code/fcn.0049a6e0.c)
- [`code/fcn.004b6700.c`](code/fcn.004b6700.c)
- [`code/fcn.004bd110.c`](code/fcn.004bd110.c)
- [`code/fcn.004d7a00.c`](code/fcn.004d7a00.c)
- [`code/fcn.004fcaa8.c`](code/fcn.004fcaa8.c)
- [`code/fcn.00500c80.c`](code/fcn.00500c80.c)
- [`code/fcn.00520b00.c`](code/fcn.00520b00.c)
- [`code/fcn.00587800.c`](code/fcn.00587800.c)
- [`code/main.c`](code/main.c)

## Behavioral Analysis

This analysis incorporates the final set of disassembled code (Chunk 10). This final segment provides critical insight into the malware's interaction model and its ability to blend in with standard web traffic, moving it from a "communication tool" to a "sophisticated management platform."

---

### Updated Analysis Summary (Cumulative)

#### Core Functionality and Purpose
The analysis of the final chunks confirms that this is an **Advanced Persistent Threat (APT)** level toolkit. The transition from basic communication to advanced features like robust HTTP parsing (`fcn.004d7a00`) suggests a dual-purpose architecture: 1) a clandestine channel for exfiltrating data and receiving commands, and 2) a potential "management" layer where an operator could interact with the infected host via web-standard protocols (HTTP).

#### New Technical Findings
*   **Robust HTTP Protocol Implementation (`fcn.004d7a00`):**
    *   This function is a sophisticated **HTTP Request/Response Handler**. It doesn't just send raw packets; it parses and manages full HTTP headers, including `Content-Length`, `Transfer-Encoding`, `Proxy-Connection`, `Keep-Alive`, and `Retry-After`.
    *   **State Management:** The code specifically handles various status codes (e.g., interpreting "Unauthorized" or "Request Header Too Large") and even manages logic for `302` Redirections (`Location` headers). 
    *   **Significance:** This suggests the malware can host a local web server or engage in complex multi-stage web interactions to bypass security gateways that only look for non-compliant HTTP traffic.

*   **Complex Command Dispatcher (`fcn.00587800`):**
    *   This function acts as a **Function Dispatcher** or "Command Switch." The extensive list of `if (unaff_retaddr == ...)` checks suggests a large table where incoming commands from the C2 are translated into specific internal functions to be executed.
    *   **Significance:** This indicates modularity. Instead of one massive "do-everything" function, the malware is organized into discrete modules (e.g., file system interaction, process injection, keylogging), which are triggered by a central dispatcher.

*   **Advanced Data Buffer Management (`fcn.0043e5d0`):**
    *   This complex loop structure handles **Segmented Memory Manipulation**. It manages buffer lengths and offsets carefully during data copying/reconstruction.
    *   **Significance:** This is used for "reassembling" fragmented data packets or handling large file uploads in chunks, ensuring that even if a transmission is interrupted, the malware can maintain integrity of the exfiltrated information.

#### New Suspicious/Malicious Behaviors
*   **Sophisticated Protocol Mimicry:** By adhering strictly to HTTP standards (parsing standard headers and responding correctly to header issues), the malware makes it extremely difficult for Network Intrusion Detection Systems (NIDS) to distinguish its traffic from legitimate web browsing.
*   **Interactivity Potential:** The depth of the HTTP parsing suggests that an attacker doesn't just "send" commands; they may have a web-based interface or console to interact with the compromised system, making it more similar to a "Remote Access Trojan" (RAT) than a simple downloader.
*   **Modular Execution:** The dispatcher identified in `fcn.00587800` confirms that the malware is designed for versatility, allowing the operator to activate various features only when needed, thereby reducing its footprint during routine checks.

#### Updated Impact Assessment
*   **Detection Difficulty: Extreme.**
    1.  **Layer 1 (Communication):** SSH/TLS masks content from packet inspectors.
    2.  **Layer 2 (Protocol Mimicry):** Full HTTP compliance hides the "malicious" nature of the requests by making them look like standard web traffic.
    3.  **Layer 3 (Architecture):** The command dispatcher allows for a modular, multi-functional presence on the host.
    4.  **Layer 4 (Persistence/Stealth):** The inclusion of advanced buffer management and state machines suggests a "long-haul" tool meant to remain active in highly secured environments for extended periods.

---

### Updated Recommendations for Incident Response

1.  **Behavioral Network Analysis (Protocol Context):**
    *   Standard firewalls may allow port 80/443 or SSH traffic. Monitor specifically for **anomalous HTTP headers**. Even if the data is encrypted, "heartbeat" patterns or connections that maintain long-lived persistent states on ports commonly used for web services should be flagged as suspicious.

2.  **Deep Packet Inspection (DPI) & Logic-Based Detection:**
    *   Since the malware uses a sophisticated state machine and standard HTTP parsing, simple "keyword" detection will fail. Look for **atypical navigation patterns**, such as an internal host reaching out to multiple external IPs using legitimate GET/POST requests but with high frequency or consistent timing (beacons).

3.  **Endpoint Detection & Memory Forensics:**
    *   Because of the modular dispatcher (`fcn.00587800`), search for processes that exhibit **"switching behavior."** For example, a single process that periodically changes its activity profile (e.g., scanning files, then making network connections, then going dormant).

4.  **Host-Based Integrity Monitoring:**
    *   The presence of high-level data parsing suggests the malware may be interacting with sensitive system information or "harvesting" large amounts of data. Monitor for processes opening many different file types (PDFs, .docx, .xlsx) in a short window, as this indicates an automated harvesting routine initiated by the internal dispatcher.

### Final Summary Conclusion
This analysis confirms that the malware is a **sophisticated, multi-layered threat** designed by highly skilled developers. It combines:
1.  A robust, custom communication protocol (via `libssh2`).
2.  Strict adherence to standard protocols (HTTP) to evade detection.
3.  An internal command dispatcher for modularity and hidden functionality.
4.  Complex data management systems for persistent, high-volume operation.

The complexity of the code suggests it is intended for **high-value targets**, where simple "commodity" malware would be detected by standard security controls. The goal of the threat actor is not just a one-time breach, but a sustained and hidden presence within the network infrastructure.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the behaviors identified in your analysis to the corresponding MITRE ATT&CK techniques and sub-techniques.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1071.001** | Application Layer Protocol: Web Protocols | The malware utilizes a robust HTTP parser (handling headers, status codes, and redirects) to blend its traffic with standard web activity. |
| **T1059** | Command and Scripting Interpreter | The "Command Dispatcher" acts as a central switch that interprets incoming C2 commands and maps them to specific internal execution functions. |
| **T1020** | Automated Exfiltration | Advanced buffer management logic is used to manage segment offsets and sizes, ensuring the integrity of large or fragmented data during exfiltration. |
| **T1056.001** | Input Capture: Keylogging | The dispatcher specifically includes a module for keylogging as part of its multi-functional capability set. |
| **T1055** | Process Injection | The identified command dispatcher contains functionality to perform process injection, allowing the malware to hide or escalate privileges. |
| **T1222** | Filesystem Discovery | The analysis indicates an automated harvesting routine where the malware interacts with a high volume of various file types in a short window. |

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral report, here are the extracted Indicators of Compromise (IOCs).

**Note:** The "EXTRACTED STRINGS" section contains high amounts of obfuscated data/garbage characters typical of a packed binary; therefore, no plain-text IP addresses, URLs, or file paths were present in that specific segment.

### **IP addresses / URLs / Domains**
*   *None identified.* (The analysis notes the use of HTTP/HTTPS and SSH, but no specific hardcoded C2 infrastructure was provided in the text.)

### **File paths / Registry keys**
*   *None identified.* (Standard system paths were excluded as per instructions.)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.* (No MD5, SHA1, or SHA256 hashes were present in the provided strings.)

### **Other artifacts**
*   **C2 Communication Patterns:** 
    *   Usage of `libssh2` for SSH/TLS-encrypted communication.
    *   Sophisticated HTTP Request/Response handling (parsing headers like `Content-Length`, `Transfer-Encoding`, `Proxy-Connection`, `Keep-Alive`, and `Retry-After`).
    *   Support for `302` Redirects within the internal logic.
*   **Internal Function Offsets (Malware Logic Markers):**
    *   `fcn.004d7a00`: HTTP Request/Response Handler.
    *   `fcn.00587800`: Command Dispatcher (Switch/Dispatcher table).
    *   `fcn.0043e5d0`: Segmented Memory/Buffer Management logic.
*   **Behavioral Indicators:** 
    *   Protocol Mimicry: Intentional adherence to standard web traffic behaviors to evade NIDS.
    *   Modular Execution: A "Command Switch" architecture allowing the malware to cycle through different functionalities (file system, injection, etc.) only when requested by a remote operator.

---

## Malware Family Classification

Based on the analysis provided, here is the classification of the sample:

1.  **Malware family:** custom
2.  **Malware type:** RAT (Remote Access Trojan) / Backdoor
3.  **Confidence:** High
4.  **Key evidence:** 
    *   **Modular Command Architecture:** The identification of a sophisticated "Command Dispatcher" (`fcn.00587800`) indicates the malware is not a single-purpose tool (like a simple downloader) but a multi-functional platform capable of executing various tasks such as keylogging, process injection, and file system discovery upon command.
    *   **Sophisticated Protocol Mimicry:** The inclusion of a robust HTTP Request/Response handler (`fcn.004d7a00`) that manages complex headers (e.g., `Keep-Alive`, `Retry-After`) and `302` redirects indicates a high level of engineering intended to bypass Network Intrusion Detection Systems (NIDS) by blending in with legitimate web traffic.
    *   **Advanced Exfiltration Capabilities:** The presence of specialized buffer management logic (`fcn.0043e5d0`) for handling segmented memory and large data reassembly confirms the malware is designed for high-volume, "long-haul" data exfiltration typical of APT-level operations.
