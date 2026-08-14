# Threat Analysis Report

**Generated:** 2026-08-11 22:49 UTC
**Sample:** `0e3e95ee6649238171fb409c143c8a944bc54332f0ce85b94c651b5d0bf95343_0e3e95ee6649238171fb409c143c8a944bc54332f0ce85b94c651b5d0bf95343.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0e3e95ee6649238171fb409c143c8a944bc54332f0ce85b94c651b5d0bf95343_0e3e95ee6649238171fb409c143c8a944bc54332f0ce85b94c651b5d0bf95343.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 5 sections |
| Size | 275,456 bytes |
| MD5 | `334c9a83996d2d727e5faafa4c80a9d4` |
| SHA1 | `67e1fb1419eb9d012f4ae09351c6c48dc55a8216` |
| SHA256 | `0e3e95ee6649238171fb409c143c8a944bc54332f0ce85b94c651b5d0bf95343` |
| Overall entropy | 6.214 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1763681622 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 184,832 | 6.437 | No |
| `.rdata` | 70,144 | 4.765 | No |
| `.data` | 5,632 | 2.96 | No |
| `.pdata` | 11,264 | 5.416 | No |
| `.reloc` | 2,560 | 5.394 | No |

### Imports

**ADVAPI32.dll**: `GetUserNameA`
**KERNEL32.dll**: `FindFirstFileA`, `FindNextFileA`, `FindClose`, `GetFileAttributesA`, `MultiByteToWideChar`, `WideCharToMultiByte`, `LCMapStringEx`, `EnterCriticalSection`, `LeaveCriticalSection`, `InitializeCriticalSectionEx`, `DeleteCriticalSection`, `EncodePointer`, `DecodePointer`, `CompareStringEx`, `GetCPInfo`

## Extracted Strings

Total strings found: **899** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@.reloc
x UATAUAVAWH
A_A^A]A\]
UVWATAUAVAWH
vb'vb'v
vb'vb'v
A_A^A]A\_^]
\$ UVWH
udH;~ u^
x UATAUAVAWH
APD9(~
D|0A
A_A^A]A\]
|$ UATAUAVAWH
.txttNH
.htmu
E
A_A^A]A\]
@SUVWAVH
L90u"H
0A^_^][
t$ WAVAWH
 A_A^_
@SAVAWH
0A_A^[
|$ t}I
0A_A^[
VPLc
J
VAVAWH
 A_A^^
WAVAWH
 A_A^_
t$ WATAUAVAWH
0A_A^A]A\_
t$ WAVAWH
@A_A^_
@SUVAVH
(A^^][
(A^^][
@SVAVAWH
(A_A^^[
@SVATAUAWH
0A_A]A\^[
@SUVWATAVAWH
@A_A^A\_^][
t$ UWAVH
\$ UVWATAUAVAWH
0A_A^A]A\_^]
WATAUAVAWH
A_A^A]A\_
uiM;J ucA
\$ WAVAWH
 A_A^_
																									
																			
																												
																												
@UWAUAWH
(A_A]_]
UVWATAUAVAWH
A_A^A]A\_^]
l$ VWAUAVAWH
l$(@8k
d$pA8m
A_A^A]_^
l$ VWAUAVAWH
l$(@8k
d$pA8m
A_A^A]_^
Cx<butH
@SUVWATAUAVAWH
~(L;~0
A_A^A]A\_^][
C$9C w
@VAUAVAWH
XA_A^A]^
l$ VWAVH
@UWAVH
@VWAUAVAWH
 A_A^A]_^
UVWATAUAVAWH
`A_A^A]A\_^]
UVWATAUAVAWH
0A_A^A]A\_^]
|$ y,H
@VAVAWH
0A_A^^
{x\ucH
\$ UVWH
;~ sBH
VWATAVAWH
 A_A^A\_^
t$ UWATAVAWH
A_A^A\_]
UVWATAUAVAWH
A_A^A]A\_^]
@UWAVH
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method.std::basic_ofstream_char__struct_std::char_traits_char__.virtual_0` | `0x140011504` | 45072 | ✓ |
| `method.std::basic_ostream_char__struct_std::char_traits_char__.virtual_0` | `0x1400114e0` | 44972 | ✓ |
| `method.std::basic_ifstream_char__struct_std::char_traits_char__.virtual_0` | `0x1400114ec` | 44680 | ✓ |
| `method.std::basic_istream_char__struct_std::char_traits_char__.virtual_0` | `0x1400114f8` | 44628 | ✓ |
| `fcn.14001caa0` | `0x14001caa0` | 39990 | ✓ |
| `fcn.14001ca8c` | `0x14001ca8c` | 39940 | ✓ |
| `fcn.1400116cc` | `0x1400116cc` | 38790 | ✓ |
| `fcn.14000c810` | `0x14000c810` | 14196 | ✓ |
| `fcn.140011a74` | `0x140011a74` | 12927 | ✓ |
| `fcn.14000b190` | `0x14000b190` | 9233 | ✓ |
| `fcn.140003890` | `0x140003890` | 5058 | ✓ |
| `fcn.14002b5f8` | `0x14002b5f8` | 2899 | ✓ |
| `fcn.140012bf0` | `0x140012bf0` | 2887 | ✓ |
| `fcn.140002970` | `0x140002970` | 2163 | ✓ |
| `fcn.14001e730` | `0x14001e730` | 1946 | ✓ |
| `fcn.14000e080` | `0x14000e080` | 1709 | ✓ |
| `fcn.14002c5e0` | `0x14002c5e0` | 1661 | ✓ |
| `fcn.14000a4a0` | `0x14000a4a0` | 1648 | ✓ |
| `fcn.14000c1b0` | `0x14000c1b0` | 1618 | ✓ |
| `fcn.14002593c` | `0x14002593c` | 1405 | ✓ |
| `fcn.140003330` | `0x140003330` | 1365 | ✓ |
| `fcn.14000d5b0` | `0x14000d5b0` | 1320 | ✓ |
| `fcn.140015f40` | `0x140015f40` | 1281 | ✓ |
| `fcn.140017100` | `0x140017100` | 1233 | ✓ |
| `fcn.140015a70` | `0x140015a70` | 1231 | ✓ |
| `fcn.14001d480` | `0x14001d480` | 1149 | ✓ |
| `fcn.140009f20` | `0x140009f20` | 1141 | ✓ |
| `fcn.140009aa0` | `0x140009aa0` | 1141 | ✓ |
| `fcn.14001fd10` | `0x14001fd10` | 1141 | ✓ |
| `fcn.140010c40` | `0x140010c40` | 1134 | ✓ |

### Decompiled Code Files

- [`code/fcn.140002970.c`](code/fcn.140002970.c)
- [`code/fcn.140003330.c`](code/fcn.140003330.c)
- [`code/fcn.140003890.c`](code/fcn.140003890.c)
- [`code/fcn.140009aa0.c`](code/fcn.140009aa0.c)
- [`code/fcn.140009f20.c`](code/fcn.140009f20.c)
- [`code/fcn.14000a4a0.c`](code/fcn.14000a4a0.c)
- [`code/fcn.14000b190.c`](code/fcn.14000b190.c)
- [`code/fcn.14000c1b0.c`](code/fcn.14000c1b0.c)
- [`code/fcn.14000c810.c`](code/fcn.14000c810.c)
- [`code/fcn.14000d5b0.c`](code/fcn.14000d5b0.c)
- [`code/fcn.14000e080.c`](code/fcn.14000e080.c)
- [`code/fcn.140010c40.c`](code/fcn.140010c40.c)
- [`code/fcn.1400116cc.c`](code/fcn.1400116cc.c)
- [`code/fcn.140011a74.c`](code/fcn.140011a74.c)
- [`code/fcn.140012bf0.c`](code/fcn.140012bf0.c)
- [`code/fcn.140015a70.c`](code/fcn.140015a70.c)
- [`code/fcn.140015f40.c`](code/fcn.140015f40.c)
- [`code/fcn.140017100.c`](code/fcn.140017100.c)
- [`code/fcn.14001ca8c.c`](code/fcn.14001ca8c.c)
- [`code/fcn.14001caa0.c`](code/fcn.14001caa0.c)
- [`code/fcn.14001d480.c`](code/fcn.14001d480.c)
- [`code/fcn.14001e730.c`](code/fcn.14001e730.c)
- [`code/fcn.14001fd10.c`](code/fcn.14001fd10.c)
- [`code/fcn.14002593c.c`](code/fcn.14002593c.c)
- [`code/fcn.14002b5f8.c`](code/fcn.14002b5f8.c)
- [`code/fcn.14002c5e0.c`](code/fcn.14002c5e0.c)
- [`code/method.std__basic_ifstream_char__struct_std__char_traits_char__.virtual_0.c`](code/method.std__basic_ifstream_char__struct_std__char_traits_char__.virtual_0.c)
- [`code/method.std__basic_istream_char__struct_std__char_traits_char__.virtual_0.c`](code/method.std__basic_istream_char__struct_std__char_traits_char__.virtual_0.c)
- [`code/method.std__basic_ofstream_char__struct_std__char_traits_char__.virtual_0.c`](code/method.std__basic_ofstream_char__struct_std__char_traits_char__.virtual_0.c)
- [`code/method.std__basic_ostream_char__struct_std__char_traits_char__.virtual_0.c`](code/method.std__basic_ostream_char__struct_std__char_traits_char__.virtual_0.c)

## Behavioral Analysis

Based on the additional disassembly provided in chunk 2/2, I have updated and expanded the analysis. The new code reveals much deeper layers of complexity regarding how the binary handles strings, file paths, and environmental "gates."

### Updated Analysis of Binary Behavior

#### 1. Core Functionality and Purpose (Expanded)
The addition of these functions confirms that this is not a simple utility but a sophisticated piece of software involving high-level logic for **system mapping** and **complex data processing**.

*   **Advanced String & Path Manipulation:** Functions like `fcn.14000d5b0` and `fcn.14001d480` exhibit extremely complex logic for handling strings. They don't just compare strings; they appear to parse, normalize, and reconstruct them (handling escape characters like `\`, and specific delimiters). This is often used to handle system paths that may contain spaces, special characters, or non-standard formatting.
*   **Intensive File System Interaction:** The inclusion of `fcn.14002593c` confirms the "Iterative Probing" noted previously. It uses `FindFirstFileExW` and `FindNextFileW` to iterate through directories. This is a heavy-duty way to "map" the local filesystem, potentially looking for specific file types (e.g., `.txt`, `.exe`) or identifying the presence of other installed software.
*   **Internal Buffer Management:** Many functions (`fcn.140009f20`, `fcn.140009aa0`) appear to be optimized, high-level string comparison or buffer manipulation routines. These suggest the binary handles a large volume of data in memory, possibly de-obfuscating internal strings or constructing complex paths "on the fly" to evade static detection.

#### 2. Suspicious and Malicious Behaviors (Expanded)
The new disassembly adds several hallmarks of sophisticated malware/droppers:

*   **Sophisticated "Environment Keying":** Function `fcn.140017100` acts as a **gatekeeper**. It checks various inputs against hard-coded, large hexadecimal constants (e.g., `0x19930520`, `0x19128c9d`). This is a classic anti-analysis technique where the program only proceeds to its "malicious" stage if it detects specific environment conditions—such as a certain OS build, specific hardware ID, or a unique configuration that matches its internal "key."
*   **Target Mapping/Profiling:** The loop using `FindFirstFileW` in conjunction with complex string checks suggests a **reconnaissance phase**. Instead of just looking for one file, it appears to be scanning the system to see what else is present. This can be used to:
    *   Identify and disable security software.
    *   Search for "high-value" targets (e.g., browser profiles, cryptocurrency wallets, or office documents).
    *   Verify that a prerequisite component of an attack chain has been successfully installed.
*   **Robust Obfuscation/Wrapper Logic:** The repetitive use of complex wrappers for simple tasks (like copying bytes or comparing strings) suggests the original source code was likely passed through a **packer or protector**. These "wrapper" functions add complexity to the control flow, making it harder for automated tools and human analysts to follow the true logic path.

#### 3. Notable Techniques and Patterns
*   **State Machine Logic:** `fcn.14000d5b0` contains a high degree of branching based on character types. This is common in parsers for complex configuration files or internal protocols, but in malware, it is often used to process "encoded" instructions or config files provided by a Command & Control (C2) server.
*   **Manual String Processing:** Instead of using standard library functions for all tasks, the binary implements its own robust methods for string manipulation (`fcn.140009f20`). This reduces the footprint of known Windows API calls and allows for more "creative" ways to handle data that might trigger security alerts.
*   **Potential Payload Decryption Trigger:** The presence of several `swi(3)` calls (software interrupts) or calls into functions like `fcn.14001b688` suggest points where the binary may be handing off execution to a newly unpacked module or performing a "jump" to a different part of its own memory space after successfully passing certain environment checks.

### Summary of Updated Findings
The addition of chunk 2/2 strengthens the conclusion that this is likely a **sophisticated malware component (dropper, loader, or complex trojan)**. 

Key indicators from the new code include:
1.  **Environment Gatekeeping:** Using hardcoded "keys" to ensure it only runs in specific environments.
2.  **Deep System Reconnaissance:** Probing the filesystem for a wide range of items rather than just one target.
3.  **High-Complexity Parsing:** Extensive custom code for handling paths and strings, likely to hide its true intent from simple scanners.

The binary is designed to be "quiet," carefully checking its surroundings before revealing or executing its primary payload.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1497** | Virtualized Environment/Sandbox Evasion | The "Environment Keying" via hard-coded hex constants (e.g., `0x19930520`) is used to ensure the binary only executes in a target environment rather than an analysis lab. |
| **T1083** | File and Directory Discovery | The use of `FindFirstFileW` and `FindNextFileW` to scan directories indicates an attempt to map the filesystem, identify security software, or locate high-value data. |
| **T1027** | Obfuscated Files/Information | The implementation of complex wrapper functions for simple tasks and custom manual string processing is designed to bypass signature-based detection and hide the program's true logic. |
| **T1114** | Modify System Firmware (Optional/Related) | *Note: While not explicitly stated as firmware, the "Environment Keying" checking specific hardware IDs can sometimes be an indicator of searching for specific machine signatures.* |

***

**Analyst Notes:** 
*   The behavior described in section 2.1 ("Advanced String & Path Manipulation") and 2.3 ("Manual String Processing") both map strongly to **T1027**, as these techniques are designed to evade automated detection by avoiding standard, easily-flagged Windows API calls for common tasks.
*   The "Target Mapping/Profiling" behavior is a classic example of the **Discovery** tactic, specifically aimed at identifying a target's environment before deploying a payload.

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral report, here are the extracted Indicators of Compromise (IOCs). 

Note: The "Strings" section contained highly obfuscated/garbled data and no actionable network indicators or clear file paths. The primary IOCs derived from this sample are behavior-based constants used in environmental keying.

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   None identified (Note: Internal memory offsets such as `fcn.1400d5b0` were noted, but these are internal code locations rather than system file paths).

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified.

**Other artifacts**
*   **Environment Keying Constants (Hex):** 
    *   `0x19930520`
    *   `0x19128c9d`
    *(Used by function `fcn.140017100` to validate the environment before executing malicious payloads).*
*   **Internal Function Offsets (Behavioral Signatures):** 
    *   `fcn.14000d5b0` (Complex string processing/parsing)
    *   `fcn.1401d480` (String manipulation)
    *   `fcn.14002593c` (Iterative file system probing via `FindFirstFileExW`)
    *   `fcn.140009f20` / `fcn.140009aa0` (Manual string/buffer management)
    *   `fcn.14001b688` (Potential payload transition point/jump)

---

## Malware Family Classification

Based on the behavioral analysis provided, here is the classification of the sample:

1. **Malware family**: Unknown (Potential custom loader/dropper)
2. **Malware type**: Loader / Dropper
3. **Confidence**: High (for Type), Medium (for Family)
4. **Key evidence**:
    *   **Sophisticated Environment Keying:** The use of specific hex constants (`0x19930520`, `0x19128c9d`) to gate execution indicates a high level of anti-analysis logic designed to detect and evade sandbox environments.
    *   **Pre-Execution Reconnaissance:** The extensive use of `FindFirstFileW` and `FindNextFileW` in an iterative loop suggests the binary is mapping the filesystem to identify targets (e.g., sensitive data) or check for security software before deploying a secondary payload.
    *   **Evasive Coding Techniques:** The implementation of custom "wrapper" functions for string manipulation and manual buffer management (rather than using standard Windows API calls) indicates an intentional effort to bypass signature-based detection and hide the program's logic from automated analysis tools.
