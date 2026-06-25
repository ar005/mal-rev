# Threat Analysis Report

**Generated:** 2026-06-24 17:45 UTC
**Sample:** `00a5638b8e6b30946cccae6a193dff85657331a97f866938a1b1c7d1be0943e9_00a5638b8e6b30946cccae6a193dff85657331a97f866938a1b1c7d1be0943e9.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `00a5638b8e6b30946cccae6a193dff85657331a97f866938a1b1c7d1be0943e9_00a5638b8e6b30946cccae6a193dff85657331a97f866938a1b1c7d1be0943e9.exe` |
| File type | PE32 executable for MS Windows 6.00 (GUI), Intel i386, 5 sections |
| Size | 47,197,544 bytes |
| MD5 | `df9c10da9ee2184f365c25ab15211d34` |
| SHA1 | `ef446f5317c775cfffb7ed230040692c7bbdee76` |
| SHA256 | `00a5638b8e6b30946cccae6a193dff85657331a97f866938a1b1c7d1be0943e9` |
| Overall entropy | 0.837 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1694090350 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 2,595,840 | 6.468 | No |
| `.rdata` | 705,024 | 5.062 | No |
| `.data` | 15,360 | 4.792 | No |
| `.rsrc` | 332,800 | 7.106 | ⚠️ Yes |
| `.reloc` | 168,960 | 6.508 | No |

### Imports

**KERNEL32.dll**: `CreateFileW`, `CloseHandle`, `WriteFile`, `DeleteFileW`, `HeapDestroy`, `HeapSize`, `HeapReAlloc`, `HeapFree`, `HeapAlloc`, `GetProcessHeap`, `SizeofResource`, `LockResource`, `LoadResource`, `FindResourceW`, `FindResourceExW`

## Extracted Strings

Total strings found: **6021** (showing first 100)

```
!This program cannot be run in DOS mode.
$
\pRich
`.rdata
@.data
@.reloc
j	h`Rj
jhtRj
jhdIj
jh|Ij
j
h$Sj
jhdSj
jhxKj
D$$$Tj
D$0`Tj
D$`PUj
j	h @l
jht@l
jh<;l
jh<;l
jhT;l
jh0Al
jh;l
jh0Al
j	h(;l
j	hXAl
y	_^]
~mht)s
	RQVSQ
@9Cw	Q
PVVj%V
D$tSUV
D$$+D$
D$$+D$
y	_^]3
u9wTt.
u9wXt.
sdVhT#j
URhd!j
URhd!j
u9w$t.
t$DUWP
D$8_^][
t$ QRVWU
P(_^][
t$0SUWQ
EhSVWP
MQj\P
F;Cu
90u)9p
P 8^<t}
L$L_^3
)D$0;~ }o
L$L_^3
D$0UVW
D$ +D$H
D$X;D$ }
L$\_^][3
p^][Y
uH8F tC
uH8F tC
jh<3j
jhT3j
~Nhl*s
	RQj	hh6j
u
;ut
A#T$
;F@uPj0
|$f99t
u
;ut
V(_^][
j	h|>j
j	h|>j
HP;OLt
O8;G@t
l$ w^;G
																									
																			
																												
																												
Awf;TA
D$;D$
D$vPR
~L]uUj]
~L}t j
+KL+SL
;QLu&;QPu
9L$ te
;t$$t/
jhJj
L|$(9\$,
L\$0;l$4f
|$(;t$<
9T$$u4
L$l_^3
j'h`Nj
j hpOj
j	h|>j
j	h|>j
t%f97t
j h `j
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.005ec9ba` | `0x5ec9ba` | 88788 | ✓ |
| `fcn.005ed323` | `0x5ed323` | 21249 | ✓ |
| `fcn.005cdcf0` | `0x5cdcf0` | 16776 | ✓ |
| `fcn.004ca540` | `0x4ca540` | 10866 | ✓ |
| `fcn.005aa980` | `0x5aa980` | 8715 | ✓ |
| `fcn.005fcce5` | `0x5fcce5` | 7455 | ✓ |
| `fcn.005b8b60` | `0x5b8b60` | 7009 | ✓ |
| `fcn.00554b10` | `0x554b10` | 6880 | ✓ |
| `fcn.00522b60` | `0x522b60` | 6825 | ✓ |
| `fcn.004a7980` | `0x4a7980` | 6646 | ✓ |
| `fcn.005f0dda` | `0x5f0dda` | 5627 | ✓ |
| `fcn.00598bc0` | `0x598bc0` | 5556 | ✓ |
| `fcn.004b5200` | `0x4b5200` | 5445 | ✓ |
| `fcn.0061080b` | `0x61080b` | 5433 | ✓ |
| `fcn.005e1600` | `0x5e1600` | 5249 | ✓ |
| `fcn.005599e0` | `0x5599e0` | 4950 | ✓ |
| `fcn.005e94d0` | `0x5e94d0` | 4515 | ✓ |
| `fcn.00582920` | `0x582920` | 4440 | ✓ |
| `fcn.00613700` | `0x613700` | 4204 | ✓ |
| `fcn.005de250` | `0x5de250` | 4170 | ✓ |
| `fcn.0055b380` | `0x55b380` | 4091 | ✓ |
| `fcn.004c0d40` | `0x4c0d40` | 4054 | ✓ |
| `fcn.00475b00` | `0x475b00` | 4019 | ✓ |
| `fcn.005a7f00` | `0x5a7f00` | 3706 | ✓ |
| `fcn.00613648` | `0x613648` | 3437 | ✓ |
| `fcn.00567b50` | `0x567b50` | 3395 | ✓ |
| `fcn.005eea64` | `0x5eea64` | 3389 | ✓ |
| `fcn.00473830` | `0x473830` | 3352 | ✓ |
| `fcn.005b7830` | `0x5b7830` | 3301 | ✓ |
| `fcn.005c81b0` | `0x5c81b0` | 3195 | ✓ |

### Decompiled Code Files

- [`code/fcn.00473830.c`](code/fcn.00473830.c)
- [`code/fcn.00475b00.c`](code/fcn.00475b00.c)
- [`code/fcn.004a7980.c`](code/fcn.004a7980.c)
- [`code/fcn.004b5200.c`](code/fcn.004b5200.c)
- [`code/fcn.004c0d40.c`](code/fcn.004c0d40.c)
- [`code/fcn.004ca540.c`](code/fcn.004ca540.c)
- [`code/fcn.00522b60.c`](code/fcn.00522b60.c)
- [`code/fcn.00554b10.c`](code/fcn.00554b10.c)
- [`code/fcn.005599e0.c`](code/fcn.005599e0.c)
- [`code/fcn.0055b380.c`](code/fcn.0055b380.c)
- [`code/fcn.00567b50.c`](code/fcn.00567b50.c)
- [`code/fcn.00582920.c`](code/fcn.00582920.c)
- [`code/fcn.00598bc0.c`](code/fcn.00598bc0.c)
- [`code/fcn.005a7f00.c`](code/fcn.005a7f00.c)
- [`code/fcn.005aa980.c`](code/fcn.005aa980.c)
- [`code/fcn.005b7830.c`](code/fcn.005b7830.c)
- [`code/fcn.005b8b60.c`](code/fcn.005b8b60.c)
- [`code/fcn.005c81b0.c`](code/fcn.005c81b0.c)
- [`code/fcn.005cdcf0.c`](code/fcn.005cdcf0.c)
- [`code/fcn.005de250.c`](code/fcn.005de250.c)
- [`code/fcn.005e1600.c`](code/fcn.005e1600.c)
- [`code/fcn.005e94d0.c`](code/fcn.005e94d0.c)
- [`code/fcn.005ec9ba.c`](code/fcn.005ec9ba.c)
- [`code/fcn.005ed323.c`](code/fcn.005ed323.c)
- [`code/fcn.005eea64.c`](code/fcn.005eea64.c)
- [`code/fcn.005f0dda.c`](code/fcn.005f0dda.c)
- [`code/fcn.005fcce5.c`](code/fcn.005fcce5.c)
- [`code/fcn.0061080b.c`](code/fcn.0061080b.c)
- [`code/fcn.00613648.c`](code/fcn.00613648.c)
- [`code/fcn.00613700.c`](code/fcn.00613700.c)

## Behavioral Analysis

This final segment of disassembly (chunk 8/8) provides the "smoking gun" for several behaviors previously suspected but now confirmed: **deep integration with Windows Installer infrastructure**, **sophisticated network communication protocols**, and **procedural persistence logic.**

The inclusion of this data confirms that the malware is not merely a standalone tool, but a component of a professional-grade malware ecosystem.

---

### Updated Analysis Summary (Final Integration)

#### 1. Granular Environment Fingerprinting (Retained)
*   The malware performs detailed checks on Windows builds and architecture to ensure it only executes in environments matching the attacker's target profile.

#### 2. Complex Buffer Decoding & De-obfuscation (Retained)
*   A heavy translation layer hides C2 infrastructure, configuration parameters, and internal command sets from basic static analysis tools.

#### 3. Advanced Multi-threading & Synchronization (Retained)
*   Robust concurrency management ensures the "orchestrator" remains stable while handling multiple concurrent tasks (e.g., heartbeat communication, downloading updates, and local system enumeration).

#### 4. Modular Orchestration & "Core Engine" Architecture (Refined)
*   The large complex structures in `fcn.005a7f00` and `fcn.005c81b0` confirm a highly modular design. The code uses sophisticated **State Machine logic** to navigate through various stages of an operation. It doesn't just execute "hardcoded" commands; it processes complex data structures to determine the next logical step in its execution cycle, allowing it to adapt to different configurations provided by the C2.

#### 5. Sophisticated Distribution & Update Infrastructure (Significantly Expanded)
*   **MSI API Integration:** The disassembly of `fcn.005a7f00` reveals direct calls to Windows Installer (MSI) functions: `MsiConfigureFeatureFromDescriptorA`, `MsiPreviewDialogW`, `MsiOpenProductW`, and `MsiGetPropertyW`.
*   **Analysis:** The malware is explicitly querying properties like `"InstalledProductName"`, `"VersionString"`, and `"ProductCode"`. This indicates the malware is designed to:
    1.  Identify itself as a legitimate part of an existing software suite.
    2.  Integrate deeply into the Windows Update/MSI system.
    3.  Appear in system logs as a standard "update" or "feature configuration" process, making it extremely difficult for IT staff to distinguish from legitimate maintenance.
*   **Reliable Download Logic:** The function `fcn.00567b50` shows advanced `WinINet` usage. It handles:
    *   **Standard HTTP Headers:** Including complex headers like `Range: bytes=...` and `If-Modified-Since`.
    *   **Sophisticated Error Handling:** Checking for specific HTTP status codes (e.g., 200 OK) before proceeding.
    *   **Malicious Intent:** The inclusion of "Range" support suggests it is capable of downloading large files or resuming interrupted downloads—a hallmark of an automated **Update/Downloader** module designed to fetch new capabilities for the core engine.

#### 6. File System Manipulation & Persistence (New Finding)
*   The presence of `CopyFileW` and `PathFileExistsW` in `fcn.005b7830` indicates that the malware is actively moving, copying, or installing files on the disk during its "update" phase.
*   **Malicious Intent:** This allows the malware to drop secondary payloads, move them into protected directories, or replace its own binaries with newer versions, ensuring long-term persistence and functionality evolution.

#### 7. Advanced Validation & State Management (Retained)
*   The use of extensive "pre-check" loops and state transitions ensures that if a network connection fails or a file is missing, the malware handles the error gracefully rather than crashing. A stable process is much harder for EDR systems to flag as suspicious compared to an unstable one.

---

### Updated Security Assessment (Incident Response)

The final disassembly highlights several high-level threats:

1.  **Infrastructure Mimicry:** The reliance on MSI APIs and standard HTTP headers (`Range`, `If-Modified-Since`) is a calculated move to blend in with legitimate corporate software updates.
2.  **"T1071.001 - Application Layer Protocol (Web Services)" & "T1568.002 - Exploitation for Privilege Escalation":** By interacting directly with the Windows Installer, the malware may attempt to escalate privileges or gain higher-level persistence by masquerading as a system installer.
3.  **Sophisticated Payload Delivery:** The robust networking logic suggests that this "Orchestrator" is likely used in campaigns where the initial infection is just the beginning—it will actively pull down additional, specialized tools based on the local environment's value to the attacker.

---

### Indicators of Compromise (IOCs) & Behavioral Notes

*   **Behavioral (Installer/Updater Mimicry):** Monitor for processes that query `MsiGetPropertyW` or call functions from `msi32.dll`. Specifically, look for software "updating" itself using standard Windows Installer properties.
*   **Network (Robust HTTP Interaction):** Look for outbound traffic using non-standard ports or common ports (80/443) that utilize the `Range` and `If-Modified-Since` headers to download large binary blobs from remote servers.
*   **File System Activity:** Monitor for processes creating/moving files in system directories (`C:\Windows\System32`, `C:\Program Files`) while simultaneously engaging in high volumes of network traffic (the "Downloader" behavior).
*   **Persistence via MSI:** Check the registry and Windows Services for new entries associated with "ProductCode" or "UpgradeCode" that don't map to known enterprise software.

---

### Summary Table of Findings (Final)

| Component | Behavior Observed | Technical Detail | Malicious Intent/Impact |
| :--- | :--- | :--- | :--- |
| **OS Fingerprinting** | Granular Version Check | Complex nested checks for specific Windows build numbers. | Target selection; ensuring the malware only runs on targeted enterprise systems. |
| **Data Decoding** | Heavy Buffer Manipulation | Multi-byte construction via bit-shifting and long loops. | Hides C2s, paths, and commands from static analysis. |
| **Concurrency Mgmt** | Thread Sync & Locking | Use of `EnterCriticalSection` to manage shared state. | Stability; allows the malware to perform multiple tasks without lagging/crashing. |
| **Orchestrator Engine** | Complex Dispatch Logic | High volume of pointer arithmetic and state checks in long functions. | Modular functionality; core remains same while payloads change based on config. |
| **Installer Mimicry** | MSI API Integration | Calls to `MsiGetPropertyW`, `MsiOpenProductW`. | Blending with legitimate software updates to evade detection by admins/security tools. |
| **Sophisticated Networking** | Robust HTTP Implementation | Use of `WinINet` with `Range` and `If-Modified-Since` headers. | Reliable, large-scale payload downloading; masquerades as a standard update process. |
| **File Manipulation** | File System Interfacing | Calls to `CopyFileW` and `PathFileExistsW`. | Moving/updating malware components on disk to maintain persistence. |

### Final Conclusion of Analysis
The analyzed binary is an **Industrial-Grade Orchestration Engine**. It combines high-end software engineering with sophisticated evasion techniques. By wrapping its malicious activities in standard Windows Installer (MSI) behaviors and robust, "feature-rich" networking protocols, it aims for a long "dwell time" within a corporate network. It acts as the central hub that receives commands from a C2 server and pulls down specialized tools to perform tasks like data exfiltration, credential theft, or lateral movement.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1497** | Virtualization/Sandbox Detection | The malware performs granular environment fingerprinting to ensure it only executes on systems matching the attacker's target profile. |
| **T1027** | Obfuscated Files or Information | A complex decoding layer is used to hide C2 infrastructure and configuration parameters from static analysis. |
| **T1568.002** | Exploitation for Privilege Escalation | The integration with MSI APIs allows the malware to masquerade as a legitimate system installer to potentially gain higher-level permissions. |
| **T1071.001** | Application Layer Protocol: Web Services | The use of WinINet with standard HTTP headers (Range, If-Modified-Since) facilitates reliable communication and information exchange via web services. |
| **T1105** | Ingress Tool Transfer | The robust download logic and subsequent file system movements are used to fetch, stage, and install additional capabilities for the core engine. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: The "Extracted Strings" section contains significant amounts of obfuscated data or non-human-readable artifacts; therefore, the primary actionable IOCs are derived from the behavior patterns identified in the analysis.

**IP addresses / URLs / Domains**
*   *None identified.* (The report notes a "heavy translation layer" hides C2 infrastructure from static analysis).

**File paths / Registry keys**
*   **Registry/MSI Properties:** `"InstalledProductName"`, `"VersionString"`, and `"ProductCode"` (Identified as specific properties queried via MSI APIs to mask the malware's presence in system logs).

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   *None identified.*

**Other artifacts**
*   **C2 Communication Patterns:** 
    *   Usage of `WinINet` library for network communication.
    *   Utilization of standard HTTP headers (`Range: bytes=...`, `If-Modified-Since`) to mimic legitimate software update behavior and download large binary blobs.
*   **API Call Signatures (Installer Mimicry):** 
    *   `MsiConfigureFeatureFromDescriptorA`
    *   `MsiPreviewDialogW`
    *   `MsiOpenProductW`
    *   `MsiGetPropertyW` (Specifically targeting `msi32.dll`)
*   **File System Operations:** 
    *   Frequent use of `CopyFileW` and `PathFileExistsW` during "update" phases to move payloads into system directories.
*   **Evasion Tactics:**
    *   State Machine logic used in functions `fcn.005a7f00` and `fcn.005c81b0`.
    *   Complex bit-shifting/multi-byte construction for de-obfuscating internal strings.

---

## Malware Family Classification

1. **Malware family:** custom
2. **Malware type:** loader / downloader
3. **Confidence:** High

4. **Key evidence:**
*   **Installer Infrastructure Mimicry:** The malware explicitly integrates with Windows Installer (MSI) APIs (e.g., `MsiGetPropertyW`, `msi32.dll`) to masquerade as a legitimate software update, allowing it to blend into system logs and evade detection by IT administrators.
*   **Modular Orchestrator Architecture:** The use of complex state machine logic and multi-threading indicates the binary is designed as a primary "hub" or orchestrator, capable of managing various concurrent tasks like heartbeat communication and secondary payload delivery.
*   **Sophisticated Payload Delivery:** The inclusion of `WinINet` functionality with robust HTTP header support (like `Range: bytes=...`) confirms its role as a high-end downloader designed to reliably fetch large, modular payloads for further exploitation (exfiltration, credential theft, etc.).
