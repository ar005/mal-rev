# Threat Analysis Report

**Generated:** 2026-08-17 23:47 UTC
**Sample:** `101b0c403511a6b65070a6d0473081bc2190a9ef5f5b68defd352527b9711d29_101b0c403511a6b65070a6d0473081bc2190a9ef5f5b68defd352527b9711d29.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `101b0c403511a6b65070a6d0473081bc2190a9ef5f5b68defd352527b9711d29_101b0c403511a6b65070a6d0473081bc2190a9ef5f5b68defd352527b9711d29.exe` |
| File type | PE32 executable for MS Windows 5.00 (GUI), Intel i386, 5 sections |
| Size | 1,677,312 bytes |
| MD5 | `7898d4b7182c5a7db786bf697906ad60` |
| SHA1 | `9e7f43daf938d011be0ad10fd84a142e554eb09d` |
| SHA256 | `101b0c403511a6b65070a6d0473081bc2190a9ef5f5b68defd352527b9711d29` |
| Overall entropy | 6.746 |
| Unpacked | No |

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

This final segment of disassembly provides a "smoking gun" regarding the malware's technical pedigree. The complexity of the underlying math, the robustness of the protocol parsing, and the sophisticated nature of its communication state machine confirm that this is not merely an automated worm, but a highly engineered **Command and Control (C2) framework.**

The new data allows us to refine our understanding of how the malware handles "Heavy Lifting"—the actual processing of large amounts of stolen data and the management of complex network protocols.

### New Analysis: Cryptographic Primitives & Protocol Mimicry

#### 1. High-Performance Cryptography (fcn.00587800)
The massive block of code involving repeated bitwise rotations, large constant additions (e.g., `0x3956c25b`, `0x12835b01`, `0x40000` multipliers), and XOR operations is the hallmark of **modern, high-performance cryptography**—specifically algorithms like **ChaCha20 or BLAKE2b**.

*   **Analysis:** The structure follows a "Quarter Round" pattern common in stream ciphers. These are designed to be extremely fast while providing high security.
*   **Implication:** This is not standard AES-based encryption (which would look different). The use of ChaCha-style primitives suggests the authors want to maximize throughput for exfiltrating large amounts of data while maintaining a "thin" footprint. It ensures that even if the traffic is intercepted via man-in-the-middle, it remains unintelligible without the specific keys/nonces.

#### 2. Sophisticated HTTP/1.x Parsing (fcn.004d7a00)
This function is a high-fidelity **HTTP Response Parser**. It doesn't just look for a keyword; it handles the nuances of the HTTP protocol.

*   **Analysis:** We see logic handling:
    *   **Chunked Transfer Encoding:** Parsing "chunk size" and "chunk_end."
    *   **Keep-Alive/Proxy-Connection:** Logic to manage persistent connections to keep a session open without re-handshaking.
    *   **Content-Length & Content-Type:** Verification of payload sizes before processing.
    *   **HTTP Versioning (1.0, 1.1, 2.0):** Handling various protocol versions and "Switch Proxy" (HTTP 101) scenarios.
*   **Implication:** This indicates the malware can **mimic legitimate web traffic.** By wrapping its data in standard HTTP headers, it can bypass basic security filters that only allow common web ports/protocols. It is designed to live inside a corporate network where HTTP traffic is permitted and expected.

#### 3. Advanced Buffer Management (fcn.0043e5d0)
This function deals with the "plumbing" of data movement—ensuring large buffers are copied, aligned, and managed correctly in memory.

*   **Analysis:** It includes complex logic for handling different lengths and types of internal pointers, ensuring that during the extraction or exfiltration phases, the malware doesn't crash due to buffer overflows or segmentation faults.
*   **Implication:** This suggests a **stability-first design.** The authors want the malware to run for weeks/months without crashing. It is prepared to handle files and data packets of significant size (e.g., full database dumps) by managing memory dynamically during the transmission process.

---

### Updated Summary of Findings (Cumulative)

| Feature | Analysis Status | Observation / Implication |
| :--- | :--- | :--- |
| **Malicious Intent** | **Confirmed (High)** | Sophisticated toolset for high-fidelity data theft and exfiltration. |
| **Evasion Profile** | **Critical+** | Uses a **VM Overlay** to hide logic; uses **HTTP Mimicry** to blend into normal traffic. |
| **C2 Communication** | **Robust / Stealthy** | Uses `libssh2` for secure tunnels and **advanced HTTP parsing** (Chunked, Keep-Alive) for command processing. |
| **Cryptography** | **High-End Stream Ciphers** | Implementation of ChaCha/BLAKE-style primitives ensures high-speed encryption for large data volumes. |
| **Data Handling** | **Robust Pipeline** | Multi-format parsing (`fcn.0041fef0`), normalization, and heavy buffer management to ensure "perfect" delivery. |
| **File System Mastery** | **Tape/Archive Awareness** | Integrity checks for Tar/Pax headers suggest it can bundle stolen data into professional archive formats before shipping. |

---

### Final Synthesis: The "Enterprise-Grade" Exfiltration Platform

The final pieces of the puzzle confirm that this is a high-tier threat, likely associated with a **sophisticated APT (Advanced Persistent Threat)** or a highly organized cybercriminal group specializing in industrial espionage.

1.  **Infrastructure Sophistication:** By integrating a full HTTP parser and advanced stream ciphers, the malware can operate in a "layered" manner:
    *   **Inner Layer:** Secure data processing and cryptographic wrapping of stolen files.
    *   **Outer Layer:** Wrapping that data in standard-compliant HTTP/SSH envelopes to bypass Network Intrusion Detection Systems (NIDS).
2.  **Operational Longevity:** The inclusion of "Keep-Alive" and "Chunked Encoding" means the malware is designed for **long-duration interactions.** It can maintain a persistent connection with its controller, allowing an operator to interact with the machine remotely without losing the session—a hallmark of high-end Remote Access Trojans (RATs).
3.  **Strategic Positioning:** This tool isn't just meant to "infect" a computer; it is designed to **operate within a corporate network.** It recognizes that modern security focuses on blocked ports/IPs; therefore, it uses common protocols (HTTP) and robust encryption to look like a standard web service or backend server.

### Final Recommendations for Incident Response:

1.  **Deep Packet Inspection (DPI):** Standard firewalls will likely miss this because it looks like standard HTTPS/SSH traffic. Use DPI to identify non-standard behavior *within* those tunnels, such as an unusual frequency of "Keep-Alive" heartbeats or HTTP requests that do not follow human browsing patterns.
2.  **Identify Lateral Movement:** Because the code is built for stability and robust parsing, look for signs of lateral movement using similar tools. If one machine is infected, others in the same subnet are likely targeted with high-priority data collection.
3.  **Memory Forensics:** Since much of the "dirty work" (decryption and buffer management) happens in memory to avoid leaving a footprint on the disk, prioritize memory dumps for machines showing signs of compromise to find the active encryption keys or internal C2 configuration tables.
4.  **Data Exfiltration Alerting:** Set alerts for **large outbound transfers over standard ports (80/443)** that occur during non-business hours or are directed at IP addresses with low reputation scores, even if they appear as "standard" web traffic.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1573** | Encrypted Channel | The use of high-performance stream ciphers (ChaCha20/BLAKE2b) ensures that exfiltrated data remains unintelligible to network defenders. |
| **T1071.001** | Application Layer Protocol: Web Protocols | The inclusion of a full HTTP(S) parser (handling Chunked Encoding, Keep-Alive, etc.) allows the malware to mimic legitimate web traffic to bypass filters. |
| **T1041** | Exfiltration Over C2 Channel | The "Heavy Lifting" logic and robust buffer management are specifically designed to facilitate the movement of large amounts of stolen data via established channels. |
| **T1074** | Data Staging | The ability to bundle data into professional archive formats (Tar/Pax) indicates a preparation phase where data is organized before being exfiltrated. |
| **T1568** | Hide Port | By utilizing standard web ports and mimicking common network behaviors, the malware effectively hides its activities within normal corporate traffic. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

**Note:** The "Extracted Strings" section contains primarily obfuscated data, memory offsets, and noise; no traditional network IOCs (IPs/URLs) or file system artifacts were present in that specific raw text. However, the **Behavioral Analysis** provides high-fidelity signatures for detection.

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   *None identified.* (The strings provided appear to be internal memory pointers or obfuscated constants rather than system paths).

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.* (No standard MD5, SHA-1, or SHA-256 hashes were present in the string dump).

### **Other artifacts (Behavioral Patterns & C2 Signatures)**
These indicators are based on the technical logic and protocol behaviors identified during analysis. These can be used to create YARA rules or IDS signatures:

*   **C2 Communication Patterns:**
    *   **HTTP/1.x Mimicry:** Usage of "Chunked Transfer Encoding," "Keep-Alive" headers, and "Switch Proxy" (HTTP 101) responses to blend with legitimate web traffic.
    *   **Secure Tunneling:** Use of `libssh2` for establishing secure tunnels to C2 infrastructure.
    *   **Persistence/Heartbeat:** Use of non-standard "Keep-Alive" frequencies to maintain persistent connections over long durations.

*   **Cryptographic Signatures (Internal Constants):**
    *   **Stream Cipher Implementation:** Presence of "Quarter Round" logic associated with **ChaCha20** or **BLAKE2b** algorithms.
    *   **Hardcoded Constants:** The values `0x3956c25b`, `0x12835b01`, and the multiplier `0x40000` are indicative of specific high-performance cryptographic libraries used for data exfiltration.

*   **Data Processing Artifacts:**
    *   **Archive Manipulation:** Logic specifically designed to identify and handle **Tar/Pax** headers (used for bundling stolen files before transit).
    *   **Buffer Management:** Sophisticated logic for handling large memory buffers, suggesting the capability to move multi-gigabyte data sets (e.g., database dumps).

---

## Malware Family Classification

Based on the provided analysis, here is the classification for the sample:

1. **Malware family:** Custom (Advanced C2 Framework)
2. **Malware type:** RAT (Remote Access Trojan) / Infostealer
3. **Confidence:** High
4. **Key evidence:** 
    *   **Sophisticated Infrastructure & Mimicry:** The use of high-performance stream ciphers (ChaCha/BLAKE style) combined with advanced HTTP parsing (Chunked Encoding, Keep-Alive, Proxy-Connection) indicates a professional-grade tool designed to blend seamlessly into corporate network traffic while maintaining long-term persistence.
    *   **High-Capacity Exfiltration Pipeline:** The inclusion of "Tape/Archive Awareness" (Tar/Pax headers) and advanced buffer management specifically tailored for large datasets suggests the primary objective is the systematic theft of substantial amounts of data (e.g., database dumps).
    *   **Enterprise-Grade Design:** The transition from simple automated behaviors to a robust, stateful communication machine confirms it is intended as an advanced espionage tool, likely used by an APT or highly organized criminal group for long-term and "noisy" data harvesting.
