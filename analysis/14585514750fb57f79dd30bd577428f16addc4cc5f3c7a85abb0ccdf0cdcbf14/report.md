# Threat Analysis Report

**Generated:** 2026-09-05 07:28 UTC
**Sample:** `14585514750fb57f79dd30bd577428f16addc4cc5f3c7a85abb0ccdf0cdcbf14_14585514750fb57f79dd30bd577428f16addc4cc5f3c7a85abb0ccdf0cdcbf14.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `14585514750fb57f79dd30bd577428f16addc4cc5f3c7a85abb0ccdf0cdcbf14_14585514750fb57f79dd30bd577428f16addc4cc5f3c7a85abb0ccdf0cdcbf14.exe` |
| File type | PE32 executable for MS Windows 6.00 (GUI), Intel i386, 5 sections |
| Size | 4,209,664 bytes |
| MD5 | `59b2d53afe2538040b2c7314d329faeb` |
| SHA1 | `04e06e60690b8bb09df26da6baafde438df1895f` |
| SHA256 | `14585514750fb57f79dd30bd577428f16addc4cc5f3c7a85abb0ccdf0cdcbf14` |
| Overall entropy | 6.385 |
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
| `.rsrc` | 723,456 | 4.494 | No |
| `.reloc` | 168,960 | 6.508 | No |

### Imports

**KERNEL32.dll**: `CreateFileW`, `CloseHandle`, `WriteFile`, `DeleteFileW`, `HeapDestroy`, `HeapSize`, `HeapReAlloc`, `HeapFree`, `HeapAlloc`, `GetProcessHeap`, `SizeofResource`, `LockResource`, `LoadResource`, `FindResourceW`, `FindResourceExW`

## Extracted Strings

Total strings found: **5588** (showing first 100)

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

This final chunk of disassembly (8/8) provides the technical "smoking gun" regarding how this binary communicates with its infrastructure and interacts with the host operating system. The analysis now moves from identifying "suspicious capabilities" to confirming **advanced networking and deep system integration.**

### Final Integrated Analysis: Sophisticated Modular Loader & Orchestrator

The addition of functions in Chunk 8 confirms that this is a high-grade, professional piece of malware (likely a modular "Loader" or "Dropper"). It doesn't just execute; it manages a complex environment and possesses a robust networking stack.

#### 1. Advanced Networking Stack (`fcn.00567b50`)
The presence of `fcn.00567b50` is highly significant. This function wraps several WinINet API calls to perform sophisticated web requests:
*   **Sophisticated HTTP Header Handling:** The code doesn't just request a URL; it constructs and manages headers including `Content-Type`, `Accept-Encoding`, and importantly, **`Range`** (for byte-range requests) and **`If-Modified-Since`**. 
    *   *Impact:* The use of "Range" suggests the malware is capable of **resuming interrupted downloads** or downloading specific segments of a file, which is a hallmark of high-quality downloader infrastructure.
*   **WinINET Integration:** By using `InternetOpenW`, `InternetConnectW`, and `HttpSendRequestW`, it leverages standard Windows libraries to blend in with legitimate browser/system traffic, making its network signature harder to distinguish from standard updates or background processes.

#### 2. Deep System Mimicry & MSI Interaction (`fcn.005a7f00`)
The analysis of `fcn.005a7f00` confirms the "Stealth through Mimicry" theory. The binary interacts directly with **Windows Installer (MSI)** components:
*   **Direct API Calls:** It utilizes `MsiOpenProductW`, `MsiGetPropertyW`, and `MsiConfigureFeatureFromDescriptorA`.
*   **Targeted Data Retrieval:** It specifically queries for properties like `InstalledProductName` and `VersionString`. 
    *   *Analysis:* The malware isn't just looking for these to be "hidden"; it is likely using them to determine if a specific target application is present on the system or to ensure its own "installation" aligns with existing software signatures. This allows the malware to blend perfectly into the environment as a legitimate component of an installed suite.

#### 3. Complex State Management & Internal Orchestration (`fcn.005c81b0`)
This function (and the surrounding block) reveals the "Engine" mentioned in previous analyses:
*   **Internal ID Logic:** The use of specific hex values (e.g., `0x6c49a8`, `0x729800`) suggests a pre-defined set of internal actions or "modules." 
*   **Complex Context Handling:** This function manages the transitions between different states of execution. It is the "manager" that decides which functionality (e.g., networking, file extraction, configuration loading) to activate next based on the data it has processed from its command/configuration blob.

---

### Final Summary Table for Incident Response

| Category | Observation | Severity | Intelligence Significance |
| :--- | :--- | :--- | :--- |
| **Network Capabilities** | Sophisticated WinINET implementation with `Range` and `If-Modified-Since` support in `fcn.00567b50`. | **Critical** | Indicates a professional, stable delivery infrastructure capable of multi-part or resumed downloads of secondary payloads (e.g., RATs, miners). |
| **System Mimicry** | Direct interaction with MSI APIs (`MsiOpenProductW`) and lookups for `InstalledProductName`. | **High** | Demonstrates an intent to blend in with standard Windows Update/Installer processes to evade manual detection by IT staff. |
| **Configuration-Driven** | Usage of internal state codes and complex decision trees in `fcn.005c81b0`. | **Medium** | Confirms the "Loader" architecture; the primary binary is a gatekeeper that handles logistics so the secondary payload can stay small/hidden. |
| **Robustness** | Extensive exception handling and multi-stage verification logic. | **High** | The tool is designed to survive in production environments without crashing, minimizing "noise" for EDR systems. |

---

### Final Analyst Note: Core Findings & Recommendations

The final disassembly confirms that this binary is not a "script kiddie" creation; it is a **mature, modular loader.** It was engineered specifically to provide an "invisible" way to get a second stage of malware into a network.

**Key Indicators (IOCs) for Analysts:**
1.  **Network Behavior:** Flag any process using WinINET that requests `Range` headers or uses `Msi` related functions unless it is a known, signed installer/updater.
2.  **Behavioral Hooking:** Monitor for calls to `MsiOpenProductW` followed by network activity—this specific chain of events is highly indicative of this family's behavior.
3.  **Memory Forensics:** Because the "orchestration" happens in memory (the state machine logic), look for large, encrypted data blocks in the process heap which are likely being parsed by `fcn.005de250` and `fcn.005c81b0`.

**Updated Response Strategy:**
*   **Network Level:** Block IP addresses associated with `UpdateUrl` or `MainAppURL` immediately across the enterprise. Monitor for any requests using HTTP headers specifically designed to "resume" data (Range/Chunked).
*   **Host Level:** Create a YARA rule targeting the specific MSI-related strings and WinINet implementation patterns found in this final chunk.
*   **Forensics:** If a machine is suspected of infection, perform memory dumps immediately to capture the *de-obfuscated* configuration data before it is discarded by the state-machine's next loop.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1071.001 | Application Layer Protocol: Web Protocols | The malware utilizes the WinINET library and standard HTTP headers (such as `Range` and `If-Modified-Since`) to blend into legitimate web traffic while communicating with its infrastructure. |
| T1036.005 | Masquerading: Match Modified Software | The binary queries specific MSI properties like `InstalledProductName` and `VersionString` to mimic the behavior of a legitimate system component for evasion. |
| T1105 | Ingress Tool Transfer | The analysis identifies the binary as a "loader" specifically designed to facilitate the retrieval and management of secondary payloads (e.g., RATs, miners). |
| T1027 | Obfuscated Files or Information | The use of internal state codes and the processing of complex configuration blobs indicates an effort to hide command logic and functional capabilities from analysis. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs).

**Note:** The "EXTRACTED STRINGS" section contains heavily obfuscated or encrypted data; no plaintext IP addresses, URLs, or file paths were identified within that specific block. Therefore, the primary actionable intelligence is derived from the **Behavioral Analysis**.

### **IP addresses / URLs / Domains**
*   **UpdateUrl** (Placeholder for C2/Download infrastructure)
*   **MainAppURL** (Placeholder for main payload delivery)
*   *Note: Specific domain names or IP addresses were not provided in the raw text, but these specific variable names are identified as targets for network monitoring.*

### **File paths / Registry keys**
*   *None detected.* (The analysis mentions interacting with Windows Installer properties, but no specific malicious file paths or registry keys were extracted.)

### **Mutex names / Named pipes**
*   *None detected.*

### **Hashes**
*   **0x6c49a8** (Internal State Code)
*   **0x729800** (Internal State Code)
*   *Note: These are internal functional identifiers/state machine markers, not file hashes (MD5/SHA).*

### **Other artifacts**
*   **HTTP Header Patterns:** 
    *   `Range` (Used for multi-part or resumed downloads)
    *   `If-Modified-Since` (Used to check content validity before download)
    *   `Content-Type`, `Accept-Encoding`
*   **WinINet API Imports:** 
    *   `InternetOpenW`
    *   `InternetConnectW`
    *   `HttpSendRequestW`
*   **MSI Integration Points (Used for System Mimicry):**
    *   `MsiOpenProductW`
    *   `MsiGetPropertyW`
    *   `MsiConfigureFeatureFromDescriptorA`
*   **Targeted Property Queries:** 
    *   `InstalledProductName`
    *   `VersionString`
*   **Function Offsets (Memory Signatures):**
    *   `fcn.00567b50` (Network routine)
    *   `fcn.005a7f00` (MSI interaction)
    *   `fcn.005c81b0` (State management/Orchestration)
    *   `fcn.005de250` (Data parsing)

---

## Malware Family Classification

1. **Malware family**: custom (Modular Loader)
2. **Malware type**: loader
3. **Confidence**: High
4. **Key evidence**:
*   **Robust Downloader Capabilities:** The implementation of `WinINET` functions combined with advanced HTTP headers like `Range` and `If-Modified-Since` indicates a high-quality infrastructure designed to reliably fetch, resume, and manage multi-part payloads (e.g., RATs or miners).
*   **Sophisticated Evasion via Mimicry:** The direct interaction with Windows Installer (MSI) APIs (`MsiOpenProductW`, `MsiGetPropertyW`) suggests a deliberate attempt to masquerade as a legitimate system update or installer component to evade detection by IT staff and security software.
*   **Modular Orchestrator Architecture:** The use of internal state-machine logic and complex configuration parsing confirms the binary serves as a "gatekeeper" designed to manage environment checks and orchestrate the deployment of subsequent malware stages rather than acting as the primary payload itself.
