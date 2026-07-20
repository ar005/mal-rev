# Threat Analysis Report

**Generated:** 2026-07-19 08:37 UTC
**Sample:** `08f563f3595f69870179d45cd38573312ce5911ce3c993a6567a9b001879bdda_08f563f3595f69870179d45cd38573312ce5911ce3c993a6567a9b001879bdda.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `08f563f3595f69870179d45cd38573312ce5911ce3c993a6567a9b001879bdda_08f563f3595f69870179d45cd38573312ce5911ce3c993a6567a9b001879bdda.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 7 sections |
| Size | 968,192 bytes |
| MD5 | `1787448ac43b1f17404e7a1407ef8f0e` |
| SHA1 | `4a32169e7f3a60b67e2ae86f74728542c0af08bb` |
| SHA256 | `08f563f3595f69870179d45cd38573312ce5911ce3c993a6567a9b001879bdda` |
| Overall entropy | 6.659 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1767814018 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 532,992 | 6.339 | No |
| `.rdata` | 214,016 | 6.202 | No |
| `.data` | 5,632 | 2.944 | No |
| `.pdata` | 16,384 | 5.777 | No |
| `.data` | 512 | -0.0 | No |
| `.rsrc` | 194,048 | 5.067 | No |
| `.reloc` | 3,584 | 5.187 | No |

### Imports

**KERNEL32.dll**: `HeapCreate`, `GetConsoleScreenBufferInfo`, `CreateNamedPipeA`, `HeapFree`, `SetLastError`, `EnterCriticalSection`, `GetCurrentProcess`, `GetStdHandle`, `WriteFile`, `TerminateProcess`, `GetFinalPathNameByHandleW`, `WaitForMultipleObjects`, `FindNextFileA`, `Thread32Next`, `LeaveCriticalSection`
**USER32.dll**: `PostThreadMessageA`, `SetWindowsHookExA`, `wsprintfA`, `UnhookWindowsHookEx`
**ADVAPI32.dll**: `RegQueryValueExA`, `RegOpenKeyExA`, `RegEnumValueA`, `RegEnumKeyExA`, `RegCloseKey`

## Extracted Strings

Total strings found: **2362** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@.data
@.reloc
L$ SVWH
L$ SUVWH
L$ SUVWH
D$03D$8
UVWATAUAVAWH
A_A^A]A\_^]
@SUVWATAUAVAWH
XA_A^A]A\_^][
@UVAVH
USVWATAUAVAWH
G\$hM;
A_A^A]A\_^[]
@SUVWATAUAVAWH
HA_A^A]A\_^][
UVWATAUAVAWH
A_A^A]A\_^]
@SVWATAVAWH
XA_A^A\_^[
@SVWATAVAWH
xA_A^A\_^[
D$Pt53
@USVWATAUAVAWH
A_A^A]A\_^[]
UVWAVAWH
`A_A^_^]
UVWATAUAVAWH
@A_A^A]A\_^]
UVWATAUAVAWH
A_A^A]A\_^]
UVWATAUAVAWH
A_A^A]A\_^]
@USVWATAUAVAWH
A_A^A]A\_^[]
UVWATAUAVAWH
|$0v2H
GD$xE3
A_A^A]A\_^]
@SUVWH
UVWATAUAVAWH
A_A^A]A\_^]
USVWATAUAVAWH
A_A^A]A\_^[]
@USVWAVH
D$8H;D$@t
D$PH9D$H
A^_^[]
@USVWAVH
A^_^[]
UVWAVAWH
A_A^_^]
USVWAVH
A^_^[]
USVWATAUAVAWH
hA_A^A]A\_^[]
UVWATAUAVAWH
A_A^A]A\_^]
@USVWATAUAVAWH
A_A^A]A\_^[]
UVWATAUAVAWH
A_A^A]A\_^]
UWATAVAWH
A_A^A\_]
D$HH;D$Pt
USVWATAUAVAWH
UUUUUUU
H;L$ht	L
UUUUUUU
;y s}H9T$p
G|$xL;
L$xr L
A_A^A]A\_^[]
UVWAVAWH
L9=K~

GL$@E3
GL$@E3
GL$@E3
A_A^_^]
SUVWATAUAVAWH
A_A^A]A\_^][
UVWATAUAVAWH
t$PE9/
A_A^A]A\_^]
UVWATAUAVAWH
A_A^A]A\_^]
@USVWAVAWH
A_A^_^[]
UWATAVAWH
A_A^A\_]
 prefix=L
@USVWATAUAVAWH
A_A^A]A\_^[]
@USVWATAUAVAWH
"name":"H
"path":"H
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.1400589f0` | `0x1400589f0` | 53146 | ✓ |
| `fcn.140069ef8` | `0x140069ef8` | 51723 | ✓ |
| `fcn.140069ee4` | `0x140069ee4` | 51682 | ✓ |
| `fcn.14004a700` | `0x14004a700` | 29689 | ✓ |
| `method.std::basic_ofstream_char__struct_std::char_traits_char__.virtual_0` | `0x140055e38` | 29620 | ✓ |
| `method.std::basic_ifstream_char__struct_std::char_traits_char__.virtual_0` | `0x140055e20` | 29404 | ✓ |
| `method.std::basic_ostringstream_char__struct_std::char_traits_char___class_std::allocator_char__.virtual_0` | `0x140055e44` | 29312 | ✓ |
| `method.std::basic_ostream_char__struct_std::char_traits_char__.virtual_0` | `0x140055e14` | 29024 | ✓ |
| `method.std::basic_istream_char__struct_std::char_traits_char__.virtual_0` | `0x140055e2c` | 28936 | ✓ |
| `fcn.140020a80` | `0x140020a80` | 13420 | ✓ |
| `fcn.1400590e0` | `0x1400590e0` | 12419 | ✓ |
| `fcn.1400756c0` | `0x1400756c0` | 12009 | ✓ |
| `fcn.140005e00` | `0x140005e00` | 11420 | ✓ |
| `fcn.1400585a0` | `0x1400585a0` | 10069 | ✓ |
| `fcn.1400585b0` | `0x1400585b0` | 9717 | ✓ |
| `fcn.140045e80` | `0x140045e80` | 9696 | ✓ |
| `fcn.140058590` | `0x140058590` | 8389 | ✓ |
| `fcn.1400151e0` | `0x1400151e0` | 6126 | ✓ |
| `fcn.14001d2f0` | `0x14001d2f0` | 5942 | ✓ |
| `fcn.1400184c0` | `0x1400184c0` | 5779 | ✓ |
| `fcn.14001a740` | `0x14001a740` | 5511 | ✓ |
| `fcn.14000cbc0` | `0x14000cbc0` | 4921 | ✓ |
| `fcn.140012660` | `0x140012660` | 4747 | ✓ |
| `fcn.1400770c0` | `0x1400770c0` | 4735 | ✓ |
| `fcn.140002f10` | `0x140002f10` | 4584 | ✓ |
| `fcn.14001f920` | `0x14001f920` | 4294 | ✓ |
| `fcn.140016eb0` | `0x140016eb0` | 4122 | ✓ |
| `fcn.14000fb90` | `0x14000fb90` | 4113 | ✓ |
| `fcn.14007a880` | `0x14007a880` | 3671 | ✓ |
| `fcn.14003f3e0` | `0x14003f3e0` | 3667 | ✓ |

### Decompiled Code Files

- [`code/fcn.140002f10.c`](code/fcn.140002f10.c)
- [`code/fcn.140005e00.c`](code/fcn.140005e00.c)
- [`code/fcn.14000cbc0.c`](code/fcn.14000cbc0.c)
- [`code/fcn.14000fb90.c`](code/fcn.14000fb90.c)
- [`code/fcn.140012660.c`](code/fcn.140012660.c)
- [`code/fcn.1400151e0.c`](code/fcn.1400151e0.c)
- [`code/fcn.140016eb0.c`](code/fcn.140016eb0.c)
- [`code/fcn.1400184c0.c`](code/fcn.1400184c0.c)
- [`code/fcn.14001a740.c`](code/fcn.14001a740.c)
- [`code/fcn.14001d2f0.c`](code/fcn.14001d2f0.c)
- [`code/fcn.14001f920.c`](code/fcn.14001f920.c)
- [`code/fcn.140020a80.c`](code/fcn.140020a80.c)
- [`code/fcn.14003f3e0.c`](code/fcn.14003f3e0.c)
- [`code/fcn.140045e80.c`](code/fcn.140045e80.c)
- [`code/fcn.14004a700.c`](code/fcn.14004a700.c)
- [`code/fcn.140058590.c`](code/fcn.140058590.c)
- [`code/fcn.1400585a0.c`](code/fcn.1400585a0.c)
- [`code/fcn.1400585b0.c`](code/fcn.1400585b0.c)
- [`code/fcn.1400589f0.c`](code/fcn.1400589f0.c)
- [`code/fcn.1400590e0.c`](code/fcn.1400590e0.c)
- [`code/fcn.140069ee4.c`](code/fcn.140069ee4.c)
- [`code/fcn.140069ef8.c`](code/fcn.140069ef8.c)
- [`code/fcn.1400756c0.c`](code/fcn.1400756c0.c)
- [`code/fcn.1400770c0.c`](code/fcn.1400770c0.c)
- [`code/fcn.14007a880.c`](code/fcn.14007a880.c)
- [`code/method.std__basic_ifstream_char__struct_std__char_traits_char__.virtual_0.c`](code/method.std__basic_ifstream_char__struct_std__char_traits_char__.virtual_0.c)
- [`code/method.std__basic_istream_char__struct_std__char_traits_char__.virtual_0.c`](code/method.std__basic_istream_char__struct_std__char_traits_char__.virtual_0.c)
- [`code/method.std__basic_ofstream_char__struct_std__char_traits_char__.virtual_0.c`](code/method.std__basic_ofstream_char__struct_std__char_traits_char__.virtual_0.c)
- [`code/method.std__basic_ostream_char__struct_std__char_traits_char__.virtual_0.c`](code/method.std__basic_ostream_char__struct_std__char_traits_char__.virtual_0.c)
- [`code/method.std__basic_ostringstream_char__struct_std__char_traits_char___class_std__allocator_char__.virtual_0.c`](code/method.std__basic_ostringstream_char__struct_std__char_traits_char___class_std__allocator_char__.virtual_0.c)

## Behavioral Analysis

This final analysis incorporates the disassembly provided in **chunk 7/7**. The inclusion of `fcn.14003f3e0` provides a definitive look at the malware's **environment auditing capabilities** and its interaction with the local file system to build a comprehensive profile of the victim’s security posture.

### Updated Analysis Summary
The addition of `fcn.14003f3e0` confirms that the malware utilizes a sophisticated **Environment Profiling Engine**. Beyond just collecting data (passwords, cookies), it actively audits the system for installed security software. The extensive list of antivirus-related strings (e.g., "Kaspersky", "Bitdefender", "McAfee") indicates that the malware is constructing a detailed report for the attacker regarding what protections were active or present on the host during the infection.

---

### New Technical Observations

#### 1. Extensive Security Software Mapping
The disassembly of `fcn.14003f3e0` reveals a massive array of hardcoded strings related to security products:
*   **Identified Targets:** "MsMpEng.exe" (Microsoft Defender), "avp.exe", "Kaspersky", "av_scan.exe" (Avira), "bdagent.exe" (Bitdefender), "ekrn.exe" (ESET), "mbam.exe" (Malwarebytes), "mcshield.exe" (McAfee), "ns.exe" (Norton), "savservice.exe" (Sophos), "fshoster32.exe" (F-Secure).
*   **Mechanism:** The malware doesn't just check if one antivirus is present; it has a predefined list of nearly 40 different security products and related processes.
*   **Significance:** This indicates the malware is designed to provide "intelligence" to the attacker. The report won't just say "the victim's passwords were stolen"; it will also state, "The victim was protected by [X] and [Y], but my scripts bypassed them."

#### 2. Sophisticated File System Iteration
The use of `FindFirstFileA` and `FindNextFileA` in `fcn.14003f3e0` is used to verify the presence or status of these security tools.
*   **Mechanism:** The code enters a loop where it checks for specific executables or service components. It uses internal logic (like the 0x20 offset checks) to validate whether those components are active or if their associated files are present on disk.
*   **Significance:** This is an **environmental check**. By confirming which security products are installed, the malware can adapt its behavior—or at least provide high-value telemetry to the attacker about the "hardness" of a target network.

#### 3. Robust Data Normalization & Buffer Management
The disassembly shows highly consistent patterns for handling string lengths and memory allocation (e.g., checking if `uVar17 < 0x10` before choosing a logic path, or adding offsets like `0x28`).
*   **Mechanism:** This is "defensive coding" characteristic of high-quality libraries (like C++ STL). It ensures that even if the victim has an unusually long list of software or a very specific configuration, the malware's "reporting engine" will not crash due to buffer overflows.
*   **Significance:** The stability of this code reinforces the **Malware-as-a-Service (MaaS)** profile. It is built to be reliable across thousands of different victim machines with varying configurations.

#### 4. Final Data Integration ("The Reporting Pipeline")
We can now see how the different parts of the malware connect:
1.  **Extraction:** `FindFirstFileA` gathers raw system info/files.
2.  **Validation:** The code checks specific conditions (like those in `fcn.14003f3e0`) to confirm what was found.
3.  **Normalization:** Information is converted into a uniform format using the robust buffer management we saw in previous chunks.
4.  **Packaging:** The "Report" logic (`fcn.140016eb0` from chunk 6) packages these pieces of data (Passwords + Cookies + Security Profile) into one unified exfiltration packet.

---

### Updated Summary of Malicious Behavior

| Category | Evidence from Analysis | Risk Level |
| :--- | :--- | :--- |
| **Automated Discovery** | Use of `FindFirstFileA`/`FindNextFileA` to crawl system paths for credentials and security artifacts. | **High** |
| **Security Profiling** | Hardcoded list of ~40+ antivirus/security product names (Kaspersky, Bitdefender, etc.). | **Critical** |
| **Report Generation** | Structured "report" logic that combines stolen data with system telemetry. | **High** |
| **Advanced Stability** | Professional-grade buffer management and length checks to prevent crashes during extraction. | **High** |
| **Sophisticated Profiling** | The ability to tell the attacker exactly what security software was present/defeated on a machine. | **Critical** |

---

### Conclusion Update (Chunk 7/7)

The final analysis confirms that this is not a standard "grabber" but a **sophisticated, enterprise-grade reconnaissance and exfiltration tool.**

With the inclusion of `fcn.14003f3e0`, we have identified a critical feature: **Advanced Reconnaissance.** The malware doesn't just want to steal data; it wants to map out the victim’s defenses. By identifying exactly which antivirus programs are installed, the attackers can determine how "successful" their infection was and identify targets that have weaker security.

**Final Technical Profile:**
*   **Capability:** Automated Data Scraping & Intelligence Gathering.
*   **Sophistication:** High (MaaS-level coding standards).
*   **Target Detail:** Highly specific; identifies specific brands of antivirus, firewalls, and system integrity tools.
*   **Primary Objective:** To provide a comprehensive "profile" of the victim to an attacker via a structured, machine-readable report.

**New Telltale Indicators for SOC/IR Teams:**
*   **AV Hunting:** The malware specifically targets processes like `msmpeng.exe`, `avpui.exe`, and `mbam.exe`. 
*   **Reporting Signatures:** Look for the "report" string or high-frequency calls to `FindFirstFileA` in non-standard system paths (often related to browser profiles or local app data).
*   **Sophisticated Buffer Logic:** The use of standard library-style length checks suggests a compiled C++ backend, making signature detection based on simple strings less effective than behavioral analysis of the "Report Generation" phase.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the behaviors identified in the provided analysis to the relevant MITRE ATT&CK techniques below:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1082** | System Information Discovery | The malware contains hardcoded strings for over 40 security products to map out and report the victim's defense capabilities. |
| **T1082** | System Information Discovery | The use of `FindFirstFileA` and `FindNextFileA` is utilized to crawl the file system and gather information regarding local files and environment artifacts. |
| **T1041** | Exfiltration Over C2 Channel | The "Reporting Pipeline" bundles multiple types of stolen data (passwords, cookies, and security profiles) into a unified package for exfiltration. |

---

## Indicators of Compromise

Based on the provided string data and behavioral analysis, here are the extracted Indicators of Compromise (IOCs) categorized by type.

### **IP addresses / URLs / Domains**
*   *None identified in the provided text.* (Note: While the malware includes a "Reporting Pipeline" for exfiltration, no specific C2 domains or IP addresses were present in the raw strings).

### **File paths / Registry keys**
The following are specific filenames/processes targeted by the malware’s environment profiling engine (used to determine if security software is active):
*   `MsMpEng.exe` (Microsoft Defender)
*   `avp.exe`
*   `av_scan.exe` (Avira)
*   `bdagent.exe` (Bitdefender)
*   `ekrn.exe` (ESET)
*   `mbam.exe` (Malwarebytes)
*   `mcshield.exe` (McAfee)
*   `ns.exe` (Norton)
*   `savservice.exe` (Sophos)
*   `fshoster32.exe` (F-Secure)

### **Mutex names / Named pipes**
*   *None identified in the provided text.*

### **Hashes**
*   *None identified in the provided string data.*

### **Other artifacts**
*   **Behavioral Signatures:**
    *   **Environment Profiling:** The malware performs systematic checks for ~40 different security products to map out the victim's defense posture.
    *   **File System Enumeration:** Frequent use of `FindFirstFileA` and `FindNextFileA` to crawl system paths for credentials and security artifacts.
    *   **Data Normalization/Packaging:** Evidence of a "Reporting Pipeline" (likely related to function `fcn.140016eb0`) that packages stolen data (Passwords, Cookies, Security Profiles) into a single unified exfiltration packet.
    *   **Sophisticated Buffer Management:** The use of standard-library style length checks and offset calculations (e.g., 0x28) to ensure the reporting tool does not crash when encountering long strings or complex configurations.
*   **Data Extraction Keys (Internal JSON/Structure Logic):**
    *   `name`, `path`, `user`, `pass`, `month`, `iban`, `city`.

---

## Malware Family Classification

1. **Malware family**: Infostealer
2. **Malware type**: Infostealer / Spyware
3. **Confidence**: High

4. **Key evidence**:
*   **Extensive Environment Profiling:** The inclusion of over 40 hardcoded strings for various security products (e.g., Kaspersky, Bitdefender, Sophos) indicates a sophisticated "Report" system designed to inform the attacker about the victim's defense posture and provide telemetry on how successfully the malware bypassed local security.
*   **Structured Data Exfiltration:** The existence of a "Reporting Pipeline" that aggregates disparate data points—including passwords, cookies, and IBAN/personal information—into a single, unified package for exfiltration is characteristic of enterprise-grade Infostealer tools.
*   **High Coding Sophistication (MaaS):** The use of robust buffer management, standard-library-style length checks, and specialized parsing logic indicates this is not a "script kiddie" tool but a professional product designed for stability across diverse victim environments typical of Malware-as-a-Service (MaaS) operations.
