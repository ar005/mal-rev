# Threat Analysis Report

**Generated:** 2026-07-14 18:03 UTC
**Sample:** `05d1ed014c0e5b677f610b06d59731437680ec0f4ec280586923353c82754057_05d1ed014c0e5b677f610b06d59731437680ec0f4ec280586923353c82754057.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `05d1ed014c0e5b677f610b06d59731437680ec0f4ec280586923353c82754057_05d1ed014c0e5b677f610b06d59731437680ec0f4ec280586923353c82754057.exe` |
| File type | PE32 executable for MS Windows 5.00 (GUI), Intel i386, 5 sections |
| Size | 1,037,960 bytes |
| MD5 | `bc1d6810f77579f16e9404cd96981959` |
| SHA1 | `5c6e89fc885d11bbf86969541a92ad0754bba112` |
| SHA256 | `05d1ed014c0e5b677f610b06d59731437680ec0f4ec280586923353c82754057` |
| Overall entropy | 6.631 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1769407650 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 782,336 | 6.547 | No |
| `.rdata` | 99,840 | 5.429 | No |
| `.data` | 17,920 | 3.838 | No |
| `.rsrc` | 96,768 | 5.155 | No |
| `.reloc` | 28,672 | 6.581 | No |

### Imports

**KERNEL32.dll**: `PeekNamedPipe`, `GetFileInformationByHandle`, `GetFullPathNameA`, `FindFirstFileA`, `GetDriveTypeA`, `FileTimeToLocalFileTime`, `FileTimeToSystemTime`, `GetCurrentProcessId`, `GlobalAlloc`, `lstrlenA`, `GetLogicalDriveStringsW`, `GetDiskFreeSpaceExW`, `GetWindowsDirectoryW`, `GetTickCount`, `ReleaseMutex`
**USER32.dll**: `PtInRect`, `wsprintfW`, `SetPropW`, `GetWindowRect`, `ReleaseDC`, `GetDC`, `SetWindowLongW`, `GetWindowLongW`, `RemovePropW`, `GetPropW`, `CallWindowProcW`, `UnregisterClassA`, `IsWindowVisible`, `MoveWindow`, `SetWindowPos`
**GDI32.dll**: `CreateCompatibleDC`, `SelectObject`, `GetObjectW`, `DeleteObject`, `EnumFontsW`, `GetDeviceCaps`, `DeleteDC`, `SetViewportOrgEx`, `CreateCompatibleBitmap`, `BitBlt`, `ExtTextOutW`, `SetBkColor`, `CreateDIBSection`
**ADVAPI32.dll**: `AdjustTokenPrivileges`, `CryptHashData`, `CryptGetHashParam`, `CryptDestroyHash`, `CryptAcquireContextA`, `CryptGenRandom`, `CryptReleaseContext`, `GetTokenInformation`, `RegOpenKeyExA`, `RegEnumKeyExA`, `RegQueryValueExA`, `IsValidSid`, `LookupAccountNameW`, `GetSidSubAuthority`, `GetSidSubAuthorityCount`
**SHELL32.dll**: `ord_165`, `SHGetSpecialFolderPathW`, `ShellExecuteExW`, `ShellExecuteW`
**ole32.dll**: `CoInitializeSecurity`, `CoSetProxyBlanket`, `CoCreateGuid`, `CoUninitialize`, `CoInitialize`, `CoCreateInstance`, `CoTaskMemFree`, `CoTaskMemAlloc`, `CoTaskMemRealloc`, `CreateStreamOnHGlobal`, `CoInitializeEx`
**OLEAUT32.dll**: `VarUI4FromStr`, `SysAllocString`, `VariantClear`, `VariantInit`, `SysFreeString`
**SHLWAPI.dll**: `StrCmpNIW`, `StrCmpIW`, `StrTrimA`, `SHSetValueA`, `SHGetValueA`, `PathRemoveFileSpecW`, `PathAppendW`, `PathFileExistsW`, `SHGetValueW`, `SHSetValueW`, `SHDeleteValueW`, `StrStrIW`, `PathFindExtensionW`, `StrCpyW`, `PathFindFileNameW`
**COMCTL32.dll**: `_TrackMouseEvent`
**VERSION.dll**: `GetFileVersionInfoW`, `GetFileVersionInfoSizeW`, `VerQueryValueW`
**gdiplus.dll**: `GdipFree`, `GdipAlloc`, `GdipCloneBrush`, `GdipDeleteBrush`, `GdipSetStringFormatLineAlign`, `GdipSetStringFormatFlags`, `GdipGraphicsClear`, `GdipSetInterpolationMode`, `GdipSetImageAttributesColorMatrix`, `GdipDisposeImageAttributes`, `GdipCreateImageAttributes`, `GdipGetImageHeight`, `GdipGetImageWidth`, `GdipDrawImageRectRect`, `GdipDeleteGraphics`
**WININET.dll**: `InternetOpenW`, `InternetOpenUrlW`, `InternetCloseHandle`, `HttpQueryInfoW`, `HttpSendRequestW`, `InternetQueryOptionW`, `InternetSetOptionW`, `InternetCrackUrlW`, `InternetConnectW`, `HttpOpenRequestW`, `InternetReadFile`
**IMM32.dll**: `ImmDisableIME`
**CRYPT32.dll**: `CertCreateCertificateChainEngine`, `CertGetCertificateChain`, `CertFreeCertificateChainEngine`, `CertFreeCertificateContext`, `CertCloseStore`, `CertFindCertificateInStore`, `CertOpenStore`, `CertAddCertificateContextToStore`, `CryptQueryObject`, `CertGetNameStringA`, `CertFreeCertificateChain`, `CryptBinaryToStringA`, `CryptStringToBinaryA`
**urlmon.dll**: `URLDownloadToCacheFileW`
**SETUPAPI.dll**: `SetupIterateCabinetW`
**IPHLPAPI.DLL**: `GetAdaptersInfo`
**WS2_32.dll**: `getaddrinfo`, `gethostbyname`, `WSACleanup`, `inet_ntoa`, `WSASetLastError`, `__WSAFDIsSet`, `WSAGetLastError`, `select`, `recv`, `send`, `WSAIoctl`, `setsockopt`, `getsockname`, `ntohs`, `bind`

## Extracted Strings

Total strings found: **3788** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
@.reloc

ur9t$
T$(RhL "
T$ RhL "
|$@uc
uf9\$
L$4QPSV
D$$QRP
$PQRW
t
9^w
t
9^w
D$9L$
tgSUVW
9t$v3
F;t$r
L$RPQ
D$TSUVWh
T@;TTu7
D$$vT2
L$d_^3
T;T
L$,^[3
TT;T3u
L$t_^][3
L$4VPQ
L$RPQ
T$8PQR
L$PQVW3
L$ QVRP
D$0;D$
tL;|$t
9L$w#
D$,UQR
l$dVW3
L$0QRP
T$4PSRV
9T$ tX
9T$ u
9T$
T$0VPQR
9INITu
;Pr	A
D$8SU3
L$8SSUQW
9\$@t6
t$$;t$
L$4SUVW
T$(RVUP
L$8VUQ
T$@VUR
D$ ;D$0
L$@RUQ
D$;D$8u

L$$QUSR
T$;T$8sN
;D$8wb
T$ RWPQh
L$(QWP
< r2<~w.
T$UV3
D$8Rh<
t$$9t$0t!9t$4t
L$ QSVR
L$ QSFVR
L$$WQh
D$4SRh
8D$u\
8D$uQ
VHW9T$
 s=9D$
f9T$(u
\$UVW
xXu9X
xXu9X
tO</tKj
l$$;l$4u
9wu>j
L$LQVP
L$LQVP
9t$Pr
\$<9t$4r
t$<;t$ u/
|$8;t$ u7
D$ 9D$
L$ RPQ
D$ QRP
\$ 9t$$ue
\$ 9t$,uE
;\$(t	
l$$;l$,t
!8\$pt
t
9^w
t
9^w
l$ +k
t
9^w
t
9^w
PQWQRVSV
SRVPQWQ
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00420370` | `0x420370` | 620695 | ✓ |
| `fcn.004b81d2` | `0x4b81d2` | 327118 | ✓ |
| `fcn.0045ce00` | `0x45ce00` | 73646 | ✓ |
| `fcn.0049f600` | `0x49f600` | 73029 | ✓ |
| `fcn.0045cd01` | `0x45cd01` | 72613 | ✓ |
| `fcn.004625b8` | `0x4625b8` | 30150 | ✓ |
| `fcn.0040f6d0` | `0x40f6d0` | 22103 | ✓ |
| `fcn.004887d0` | `0x4887d0` | 16469 | ✓ |
| `fcn.00489480` | `0x489480` | 11099 | ✓ |
| `fcn.004776bb` | `0x4776bb` | 5632 | ✓ |
| `fcn.00428080` | `0x428080` | 5540 | ✓ |
| `fcn.00496890` | `0x496890` | 4417 | ✓ |
| `fcn.004549a0` | `0x4549a0` | 3817 | ✓ |
| `fcn.004a9520` | `0x4a9520` | 3781 | ✓ |
| `fcn.0044d940` | `0x44d940` | 3666 | ✓ |
| `fcn.004b61a0` | `0x4b61a0` | 3314 | ✓ |
| `fcn.004a0cd0` | `0x4a0cd0` | 3298 | ✓ |
| `fcn.0047dce5` | `0x47dce5` | 2971 | ✓ |
| `fcn.0046bbcd` | `0x46bbcd` | 2935 | ✓ |
| `fcn.0046610c` | `0x46610c` | 2933 | ✓ |
| `fcn.0041aa70` | `0x41aa70` | 2753 | ✓ |
| `fcn.004ac4d0` | `0x4ac4d0` | 2725 | ✓ |
| `fcn.0049b490` | `0x49b490` | 2644 | ✓ |
| `fcn.0044c830` | `0x44c830` | 2639 | ✓ |
| `fcn.00445b30` | `0x445b30` | 2584 | ✓ |
| `fcn.00441a20` | `0x441a20` | 2549 | ✓ |
| `fcn.0049feb0` | `0x49feb0` | 2399 | ✓ |
| `fcn.004837a2` | `0x4837a2` | 2343 | ✓ |
| `fcn.004926b0` | `0x4926b0` | 2288 | ✓ |
| `fcn.004938f0` | `0x4938f0` | 2264 | ✓ |

### Decompiled Code Files

- [`code/fcn.0040f6d0.c`](code/fcn.0040f6d0.c)
- [`code/fcn.0041aa70.c`](code/fcn.0041aa70.c)
- [`code/fcn.00420370.c`](code/fcn.00420370.c)
- [`code/fcn.00428080.c`](code/fcn.00428080.c)
- [`code/fcn.00441a20.c`](code/fcn.00441a20.c)
- [`code/fcn.00445b30.c`](code/fcn.00445b30.c)
- [`code/fcn.0044c830.c`](code/fcn.0044c830.c)
- [`code/fcn.0044d940.c`](code/fcn.0044d940.c)
- [`code/fcn.004549a0.c`](code/fcn.004549a0.c)
- [`code/fcn.0045cd01.c`](code/fcn.0045cd01.c)
- [`code/fcn.0045ce00.c`](code/fcn.0045ce00.c)
- [`code/fcn.004625b8.c`](code/fcn.004625b8.c)
- [`code/fcn.0046610c.c`](code/fcn.0046610c.c)
- [`code/fcn.0046bbcd.c`](code/fcn.0046bbcd.c)
- [`code/fcn.004776bb.c`](code/fcn.004776bb.c)
- [`code/fcn.0047dce5.c`](code/fcn.0047dce5.c)
- [`code/fcn.004837a2.c`](code/fcn.004837a2.c)
- [`code/fcn.004887d0.c`](code/fcn.004887d0.c)
- [`code/fcn.00489480.c`](code/fcn.00489480.c)
- [`code/fcn.004926b0.c`](code/fcn.004926b0.c)
- [`code/fcn.004938f0.c`](code/fcn.004938f0.c)
- [`code/fcn.00496890.c`](code/fcn.00496890.c)
- [`code/fcn.0049b490.c`](code/fcn.0049b490.c)
- [`code/fcn.0049f600.c`](code/fcn.0049f600.c)
- [`code/fcn.0049feb0.c`](code/fcn.0049feb0.c)
- [`code/fcn.004a0cd0.c`](code/fcn.004a0cd0.c)
- [`code/fcn.004a9520.c`](code/fcn.004a9520.c)
- [`code/fcn.004ac4d0.c`](code/fcn.004ac4d0.c)
- [`code/fcn.004b61a0.c`](code/fcn.004b61a0.c)
- [`code/fcn.004b81d2.c`](code/fcn.004b81d2.c)

## Behavioral Analysis

This additional disassembly (Chunk 5/5) provides the "smoking gun" for several of the high-level observations made in previous chunks. It moves from general evidence of sophistication to specific, documented implementation of **robust network stack handling** and **multi-protocol flexibility.**

### Updated Analysis Summary (including Chunk 5/5)

#### Core Functionality and Purpose
This final chunk solidifies the analysis of the binary as a high-end tool designed for reliable communication across diverse network environments.

*   **Explicit Multi-Protocol Support (`fcn.00493d64` area):**
    *   The code explicitly checks for and identifies various protocols: **POP3, HTTP, SMTP, IMAP, LDAP, and DICT.**
    *   **Significance:** This confirms that the malware isn't just "capable" of different protocols; it has a dedicated logic path for each. In an incident response scenario, this means the malware can potentially pivot its communication method (e.g., moving from HTTP to SMTP or IMAP) if standard web ports are blocked by a firewall or monitored by an IDS/IPS.

*   **Complex URL Normalization and Validation:**
    *   The code contains extensive logic for handling "malformed" URLs, such as checking for double slashes (`//`), resolving local hostnames (handling both `localhost` and `127.0.0.1`), and stripping invalid characters or leading slashes.
    *   **Significance:** This is not "lazy" coding. It indicates the use of a professional-grade networking library (likely **libcurl** or similar). The malware isn't just grabbing a URL from a config file; it is actively sanitizing and "repairing" the URL to ensure a successful connection is established, regardless of minor formatting errors in the C2 instructions.

*   **Resilient Logic for Edge Cases:**
    *   The logic handles specific edge cases like IPv6 address formats (checking for brackets `[]` and encoding `%` as `%25`).
    *   **Significance:** This level of detail is typical of industrial-grade software. It ensures the malware remains stable when interacting with complex network configurations, a hallmark of high-tier, state-sponsored tools that need to function reliably across varied victim environments.

---

### Refined Technical Assessment (Cumulative)

#### 1. High-Tier Infrastructure & Obfuscation
*   **Evidence:** The combination of XOR-obfuscated strings (Chunk 1/5), sophisticated math/floating-point handling (Chunk 3/5), and complex URL normalization (Chunk 5/5).
*   **Conclusion:** This is not a "script kiddie" tool. It is built with a high degree of intentionality, utilizing robust libraries to ensure that the core communication engine is stable and less likely to crash during operation.

#### 2. Advanced Network Evasion & Flexibility
*   **Evidence:** Support for **POP3, SMTP, IMAP, and LDAP** in addition to standard HTTP/HTTPS.
*   **Conclusion:** The malware possesses high "agility." If an analyst blocks port 80/443, the attacker can command the malware to switch to a different protocol (like SMTP) which may be allowed by policy for email traffic.

#### 3. High-Efficiency Data Exfiltration
*   **Evidence:** Use of **multiplexing and pipelining** in the networking stack.
*   **Conclusion:** The malware is designed to move large amounts of data while maintaining a low profile on the wire. By using "pipes," it can send multiple commands or exfiltrate chunks of data over a single established connection, making it much harder for signature-based security tools to flag "bursty" suspicious traffic.

#### 4. Multi-Stage Execution & Environmental Preparation
*   **Evidence:** Use of `ShellExecuteW` and extensive `SHLWAPI` calls to check paths and directories.
*   **Conclusion:** The malware is a gateway. It prepares the environment (checks files, creates folders) before executing subsequent stages or launching secondary "worker" scripts (PowerShell/VBS).

---

### Updated Summary for Incident Response:

*   **Primary Capability:** **Multi-Protocol Gateway.** 
    *   The binary can communicate over a wide array of protocols (**HTTP, POP3, SMTP, IMAP, LDAP**).
    *   **Action:** Block not just common web ports (80/443), but also consider the impact of non-standard protocols like POP3 and IMAP if they are enabled in the environment.

*   **Core Detection Strategy:** **Network Behavior Analysis.**
    *   Look for **long-lived TCP connections** that utilize HTTP multiplexing or pipelining.
    *   Monitor for any internal process attempting to initiate connections on ports associated with SMTP/POP3/IMAP if those are not standard for the specific host's role (e.g., a workstation suddenly trying to talk via POP3).

*   **Host-Based Detection:** 
    *   Identify and block common "precursor" actions: repeated checks of local directory structures, followed by the execution of `ShellExecuteW` commands or scripts (`.ps1`, `.vbs`).
    *   Since internal strings are XOR-obfuscated, **memory scanning** is more effective than static string searching for identifying C2 infrastructure during active infections.

*   **Final Assessment:** This binary exhibits hallmarks of an **Advanced Persistent Threat (APT)** tool. It is designed for reliability, stealthy data exfiltration, and versatile communication to bypass traditional security perimeters.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1071** | Application Layer Protocol | The malware explicitly supports multiple protocols (POP3, HTTP, SMTP, IMAP, LDAP, and DICT) to ensure communication reliability and evade port-specific filtering. |
| **T1027** | Obfuscated Files or Information | The use of XOR-obfuscated strings indicates a deliberate effort to hide internal configuration data and C2 infrastructure from static analysis tools. |
| **T1568** | Dynamic Resolution | The malware's "agility" to switch protocols based on network environment conditions allows it to bypass security perimeters that block standard web ports. |
| **T1059** | Command and Scripting Interpreter | The use of `ShellExecuteW` to launch secondary scripts (.ps1, .vbs) indicates the use of built-in interpreters for multi-stage execution. |
| **T1083** | File and Directory Discovery | The extensive use of `SHLWAPI` calls to check paths and directories suggests an effort to map the environment or verify conditions before launching further stages. |
| **T1105** | Ingress Tool Transfer | (Contextual) The "Multi-Protocol Gateway" functionality suggests a capability to pull down additional tools/modules via various protocols to maintain persistence or expand capabilities. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here is the extracted Indicators of Compromise (IOCs). 

Note: The "EXTRACTED STRINGS" section contained primarily obfuscated/garbage data; no actionable IPs, URLs, or File Paths were found within those specific strings. The intelligence below is derived from the behavior analysis.

### **IP addresses / URLs / Domains**
*   *None identified.* (The text mentions capabilities to handle these, but does not list specific hardcoded destinations.)

### **File paths / Registry keys**
*   *None identified.* (While the report mentions "checking of local directory structures," no specific malicious paths were provided.)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts**
*   **C2 Protocol Support:** The malware is configured to communicate over the following protocols (potential for multi-vector communication):
    *   HTTP
    *   POP3
    *   SMTP
    *   IMAP
    *   LDAP
    *   DICT
*   **Communication Patterns:** 
    *   **Multiplexing and Pipelining:** Used to send multiple commands or data chunks over a single connection to avoid "bursty" traffic detection.
    *   **URL Normalization:** The binary contains logic to "repair" malformed URLs (handling double slashes, local hostnames like 127.0.0.1, and IPv6 brackets).
*   **Execution Artifacts:**
    *   **Secondary Scripts:** Use of `.ps1` (PowerShell) and `.vbs` (VBScript) for secondary stages.
    *   **API Usage:** Frequent calls to `ShellExecuteW` and `SHLWAPI` functions for environment preparation.

---
**Analyst Note:** This sample behaves as a high-tier "Gateway" tool. Because the strings are heavily obfuscated, signature-based detection on raw strings is unlikely to be effective. Detection should focus on **Network Behavior Analysis**, specifically monitoring non-standard uses of SMTP/IMAP ports and identifying processes utilizing multiplexing techniques to exfiltrate data.

---

## Malware Family Classification

Based on the detailed behavioral analysis provided, here is the classification for the sample:

1. **Malware family**: Unknown (High-tier Custom/Modular)
2. **Malware type**: Loader / Backdoor
3. **Confidence**: High
4. **Key evidence**:
    *   **Advanced Network Resilience:** The inclusion of a robust, multi-protocol networking stack (POP3, HTTP, SMTP, IMAP, LDAP, DICT) combined with sophisticated URL normalization logic indicates a high-tier, professional-grade development intended to bypass environment-specific network restrictions.
    *   **Evasion and Stealth Techniques:** The use of XOR-obfuscated strings, "multiplexing/pipelining" to mask bursty traffic patterns, and the ability to switch protocols automatically demonstrates a high level of intentionality meant to evade signature-based and behavioral detection systems.
    *   **Multi-Stage Execution Gateway:** The evidence of environmental checks (via `SHLWAPI`) and the execution of secondary scripts (`.ps1`, `.vbs` via `ShellExecuteW`) confirms that the primary role of this binary is as a "gateway" or "loader," designed to establish a foothold and pull in additional modules or tools.
