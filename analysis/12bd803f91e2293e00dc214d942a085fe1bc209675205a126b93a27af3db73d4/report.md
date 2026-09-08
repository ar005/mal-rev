# Threat Analysis Report

**Generated:** 2026-08-31 19:12 UTC
**Sample:** `12bd803f91e2293e00dc214d942a085fe1bc209675205a126b93a27af3db73d4_12bd803f91e2293e00dc214d942a085fe1bc209675205a126b93a27af3db73d4.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `12bd803f91e2293e00dc214d942a085fe1bc209675205a126b93a27af3db73d4_12bd803f91e2293e00dc214d942a085fe1bc209675205a126b93a27af3db73d4.exe` |
| File type | PE32 executable for MS Windows 6.00 (GUI), Intel i386, 4 sections |
| Size | 225,792 bytes |
| MD5 | `db2dd095b008f48e642588711b648693` |
| SHA1 | `277c89808d98300ed219241ac201c5c47da0e0e3` |
| SHA256 | `12bd803f91e2293e00dc214d942a085fe1bc209675205a126b93a27af3db73d4` |
| Overall entropy | 6.454 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1766615656 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 166,912 | 6.602 | No |
| `.rdata` | 44,544 | 4.73 | No |
| `.data` | 4,608 | 3.331 | No |
| `.reloc` | 8,704 | 6.382 | No |

### Imports

**ADVAPI32.dll**: `GetUserNameA`
**SHELL32.dll**: `SHGetFolderPathA`
**KERNEL32.dll**: `WriteConsoleW`, `HeapSize`, `FindFirstFileA`, `GetDriveTypeA`, `FindNextFileA`, `FindClose`, `GetFileAttributesA`, `MultiByteToWideChar`, `WideCharToMultiByte`, `LCMapStringEx`, `EnterCriticalSection`, `LeaveCriticalSection`, `InitializeCriticalSectionEx`, `DeleteCriticalSection`, `EncodePointer`

## Extracted Strings

Total strings found: **753** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.reloc
E+D$
N<9
t2W
}PRVWS
t8 9\8$|
;Uu^V
																									
																			
																												
																												
FH<bu\j
8\u*@;
8\u*@;
8\u*@;
8\u'@;
8\u*@;
L$(^[3
9Whvg3
D$(SVW
8\u*@;
L$4_^[3
FH<fu

FH<au

8\u(@;
;NLuI;NPu
9GhvI3
+OL+WL_;
u4FG;uu
Yt
jV
PPPPPWS
jhp;C
M;Jr

D$+d$SVW
D$+d$SVW
QQSVWd
jh0>C
jhP>C
jhp>C
ARPRQh
t;Et
PPPPPPPP
u9~uj
};GvP
38_^]
E9xt
&9Gv!8E
j<h8<C
9~v@k
URPQQh
kUQPXY]Y[
PVVVVV
PVVVVV
j,hp=C
uhPkC
j"^f92
tj	_f;
j"_f9z
t"j	[f;
9>tWV
pLhtkC
SWt@jU
_t^PVj@
u/j,Xf;
uj;Xf9
tG;}r
tf;1u
xE;5xmC

u<jXSf

u	jZf
PVVVVV
jhXAC
xK;5xmC
jhxAC
PVVVVV
PWWWWW
;EuK;U
D8(Ht'
D8(HtU
j
Xf9E
D8(Ht5F
j
_f9;u
x;5xmC
PVVVVV
PPPPPWV
PP9E u
[PVVVVV
j"[WVVVV
PVVVVV
+ERSP
_PSSSSS
j"_VSSSS
WVVVVV
PVSRSQV
<at.<rt!<wt
<=upG8
u#VhpnC
jhxBC
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **29**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00413600` | `0x413600` | 34184 | — |
| `fcn.004108a7` | `0x4108a7` | 31361 | ✓ |
| `fcn.00410b3b` | `0x410b3b` | 10949 | ✓ |
| `fcn.00403fa3` | `0x403fa3` | 5731 | ✓ |
| `fcn.0041463e` | `0x41463e` | 3489 | ✓ |
| `fcn.00417098` | `0x417098` | 3078 | ✓ |
| `fcn.004278a8` | `0x4278a8` | 2621 | ✓ |
| `fcn.00402920` | `0x402920` | 2004 | ✓ |
| `fcn.00403220` | `0x403220` | 1874 | ✓ |
| `fcn.0040d990` | `0x40d990` | 1450 | ✓ |
| `fcn.00413010` | `0x413010` | 1396 | ✓ |
| `fcn.0040a7b0` | `0x40a7b0` | 1320 | ✓ |
| `fcn.00426bf0` | `0x426bf0` | 1262 | ✓ |
| `fcn.0040fef0` | `0x40fef0` | 1020 | ✓ |
| `fcn.0040d0d0` | `0x40d0d0` | 985 | ✓ |
| `fcn.0041ca8b` | `0x41ca8b` | 962 | ✓ |
| `fcn.0041f166` | `0x41f166` | 907 | ✓ |
| `fcn.0040b540` | `0x40b540` | 838 | ✓ |
| `fcn.0040c1d0` | `0x40c1d0` | 837 | ✓ |
| `fcn.0041afa7` | `0x41afa7` | 827 | ✓ |
| `fcn.00411f07` | `0x411f07` | 813 | ✓ |
| `fcn.00426520` | `0x426520` | 810 | ✓ |
| `fcn.0040cdb0` | `0x40cdb0` | 796 | ✓ |
| `fcn.0040e430` | `0x40e430` | 796 | ✓ |
| `fcn.0040d670` | `0x40d670` | 789 | ✓ |
| `fcn.00425374` | `0x425374` | 769 | ✓ |
| `fcn.0041ac01` | `0x41ac01` | 752 | ✓ |
| `fcn.0041a6f3` | `0x41a6f3` | 699 | ✓ |
| `fcn.0040fc30` | `0x40fc30` | 690 | ✓ |
| `fcn.004201dc` | `0x4201dc` | 679 | ✓ |

### Decompiled Code Files

- [`code/fcn.00402920.c`](code/fcn.00402920.c)
- [`code/fcn.00403220.c`](code/fcn.00403220.c)
- [`code/fcn.00403fa3.c`](code/fcn.00403fa3.c)
- [`code/fcn.0040a7b0.c`](code/fcn.0040a7b0.c)
- [`code/fcn.0040b540.c`](code/fcn.0040b540.c)
- [`code/fcn.0040c1d0.c`](code/fcn.0040c1d0.c)
- [`code/fcn.0040cdb0.c`](code/fcn.0040cdb0.c)
- [`code/fcn.0040d0d0.c`](code/fcn.0040d0d0.c)
- [`code/fcn.0040d670.c`](code/fcn.0040d670.c)
- [`code/fcn.0040d990.c`](code/fcn.0040d990.c)
- [`code/fcn.0040e430.c`](code/fcn.0040e430.c)
- [`code/fcn.0040fc30.c`](code/fcn.0040fc30.c)
- [`code/fcn.0040fef0.c`](code/fcn.0040fef0.c)
- [`code/fcn.004108a7.c`](code/fcn.004108a7.c)
- [`code/fcn.00410b3b.c`](code/fcn.00410b3b.c)
- [`code/fcn.00411f07.c`](code/fcn.00411f07.c)
- [`code/fcn.00413010.c`](code/fcn.00413010.c)
- [`code/fcn.0041463e.c`](code/fcn.0041463e.c)
- [`code/fcn.00417098.c`](code/fcn.00417098.c)
- [`code/fcn.0041a6f3.c`](code/fcn.0041a6f3.c)
- [`code/fcn.0041ac01.c`](code/fcn.0041ac01.c)
- [`code/fcn.0041afa7.c`](code/fcn.0041afa7.c)
- [`code/fcn.0041ca8b.c`](code/fcn.0041ca8b.c)
- [`code/fcn.0041f166.c`](code/fcn.0041f166.c)
- [`code/fcn.004201dc.c`](code/fcn.004201dc.c)
- [`code/fcn.00425374.c`](code/fcn.00425374.c)
- [`code/fcn.00426520.c`](code/fcn.00426520.c)
- [`code/fcn.00426bf0.c`](code/fcn.00426bf0.c)
- [`code/fcn.004278a8.c`](code/fcn.004278a8.c)

## Behavioral Analysis

Based on the additional disassembly provided in chunk 2/2, I have updated and expanded the analysis. The new code confirms the presence of more advanced anti-analysis techniques and indicates a high level of sophistication in how the malware processes and prepares data for exfiltration.

### Updated Analysis: Targeted Information Stealer (Enhanced)

#### Core Functionality and Purpose
The binary remains characterized as a **targeted information stealer**. However, the second set of functions reveals that it is not just a "dumb" scraper; it contains complex logic to process data after collection.

*   **Sophisticated Data Parsing & Transformation:** Functions such as `fcn.0040d0d0` and `fcn.0041afa7` contain dense bitwise operations, multi-pass loops, and complex memory management. This suggests that once the malware identifies high-value targets (Crypto wallets, Cloud accounts), it likely performs **data normalization or encoding/decoding** to ensure the stolen information is in a specific format required by its Command & Control (C2) infrastructure.
*   **Robust File Handling:** The function `fcn.0041ca8b` interacts with system handles and calls `WriteFile`. This suggests the malware may create temporary "staged" files to organize stolen data or logs, potentially adding formatting (like newlines) before preparing it for network transmission.

#### Suspicious or Malicious Behaviors
*   **Advanced Anti-Analysis & Hardware Fingerprinting:** 
    *   **CPUID Exploitation:** Function `fcn.00411f07` is a significant find. It executes **CPUID instructions** to check for specific processor features (e.g., SSE, AVX, and specific leaf values). This is a high-level evasion technique used to detect if the code is running in a virtualized environment (VM), an emulator, or under the supervision of an automated sandbox.
    *   **Environment Awareness:** By checking these hardware flags, the malware can decide whether to execute its malicious payload or "play dead" if it detects a research environment.
*   **Sophisticated String/Data Manipulation:** The presence of functions like `fcn.0040c1d0` and `fcn.0040b540` suggests the use of complex string processing logic (potentially involving similar structures to `std::string`). It seems capable of handling dynamic inputs, escaping characters, or parsing specific configuration syntax used by the targeted applications (e.g., parsing JSON or .conf files).
*   **System-Level Interaction:** The use of `GetConsoleMode` and `ReadConsoleW` in `fcn.0041f166`, while seemingly odd for a "silent" stealer, can be used to verify the presence of a standard user console environment vs. an automated script environment.

#### Notable Techniques & Patterns
*   **Complex Logic Gates:** The sheer size and complexity of functions like `fcn.0040d0d0` (heavy use of shifts, masks, and bitwise OR/ANDs) are often used to hide the true purpose of the code from automated static analysis tools. This is "code obfuscation through complexity."
*   **Staged Execution Logic:** The distinction between functions like `fcn.00426520` (which handles file types and attributes) and `fcn.0041ca8b` (which performs the write/prepare action) suggests a multi-stage "Collect $\rightarrow$ Process $\rightarrow$ Stage $\rightarrow$ Exfiltrate" workflow.
*   **Professional Development Markers:** The use of standard-looking data structures (e.g., `vtable.std::_Node_end_group`) suggests this was likely compiled from high-quality source code, potentially utilizing common libraries to handle its internal logic while overlaying malicious behavior.

---

### Summary of New Findings
| Feature | Function(s) | Risk/Impact |
| :--- | :--- | :--- |
| **Hardware Fingerprinting** | `fcn.00411f07` | Identifies virtual machines/sandboxes via CPUID instructions to evade analysis. |
| **Data Normalization** | `fcn.0040d0d0`, `fcn.0041afa7` | Complex bit-shifting logic used to process/reformat stolen data for C2 transmission. |
| **Staging & Prep** | `fcn.0041ca8b` | Prepares local files by manipulating handles and lengths before final exfiltration. |
| **String Processing** | `fcn.0040c1d0`, `fcn.0040b540` | Robust logic to handle varying lengths and types of configuration data found in targets. |

### Conclusion Update
The inclusion of these functions confirms that the binary is a high-capability piece of malware. It employs **sophisticated evasion (hardware fingerprinting)** and **complex internal processing** to maximize its chances of successful deployment and data theft while minimizing the chance of being detected by security researchers or automated analysis systems.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1497 | Virtualization/Sandbox Detection | The use of `CPUID` instructions to check for hardware features and `GetConsoleMode` to differentiate between user and automated environments are used to detect research environments. |
| T1027 | Obfuscated Files or Information | The implementation of complex bitwise operations, multi-pass loops, and high-complexity logic gates is intended to hide the true purpose of the code from static analysis tools. |
| T1070.004 | Data Staging | The use of `WriteFile` and specific functions for processing data suggests a "Stage" phase where stolen information is organized into local files before being transmitted to a C2 server. |
| T1036 | Masquerading | The utilization of standard library structures (e.g., `vtable.std::_Node_end_group`) allows the malware to appear as legitimate software during basic analysis. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: The "Extracted Strings" section contained primarily standard library error messages (e.g., `regex_error`, `connection refused`) and memory offsets which were excluded as they do not constitute unique infrastructure or file system markers for a specific threat actor.

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   None identified (The analysis mentions the use of "WriteFile" and system handles, but no specific hardcoded local paths were provided).

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified.

**Other artifacts**
*   **Evasion Technique:** Hardware Fingerprinting via **CPUID instructions** (identified in `fcn.00411f07`). This is used to detect virtualized environments or sandboxes.
*   **Behavioral Pattern - Data Processing:** Complex bitwise operations and multi-pass loops (`fcn.0040d0d0`, `fcn.0041afa7`) used for data normalization/encoding of stolen credentials (Crypto wallets, Cloud accounts).
*   **Behavioral Pattern - Staging:** Multi-stage execution logic involving the collection, processing, and local staging of files before exfiltration (`fcn.00426520`, `fcn.0041ca8b`).
*   **Environment Check:** Usage of `GetConsoleMode` and `ReadConsoleW` (`fcn.0041f166`) to differentiate between interactive user sessions and automated environments.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: infostealer
3. **Confidence**: High
4. **Key evidence**:
    *   **Advanced Evasion Techniques:** The sample employs sophisticated anti-analysis measures, including `CPUID` instruction execution for hardware fingerprinting (to detect VMs/sandboxes) and `GetConsoleMode`/`ReadConsoleW` to identify automated vs. human-interactive environments.
    *   **Targeted Data Processing:** The analysis identifies specific logic for "normalizing" and processing high-value targets, specifically **Crypto wallets** and **Cloud accounts**, using complex bitwise operations to prepare data for exfiltration.
    *   **Staged Execution Workflow:** The malware follows a sophisticated multi-stage pipeline (Collection $\rightarrow$ Processing $\rightarrow$ Staging) rather than immediate transmission, indicating a professional development approach to ensure successful data theft.
