# Threat Analysis Report

**Generated:** 2026-09-05 21:02 UTC
**Sample:** `14af010225b7dd959745a1cece3631b9a4154c6d16143873c15b04d6a3e8f6ca_14af010225b7dd959745a1cece3631b9a4154c6d16143873c15b04d6a3e8f6ca.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `14af010225b7dd959745a1cece3631b9a4154c6d16143873c15b04d6a3e8f6ca_14af010225b7dd959745a1cece3631b9a4154c6d16143873c15b04d6a3e8f6ca.exe` |
| File type | PE32+ executable for MS Windows 5.02 (GUI), x86-64 (stripped to external PDB), 10 sections |
| Size | 842,240 bytes |
| MD5 | `1595f4b9cccabe80b6546ccd1290738c` |
| SHA1 | `3470a95ad0dacf62aa83c47543180ad29bf36d24` |
| SHA256 | `14af010225b7dd959745a1cece3631b9a4154c6d16143873c15b04d6a3e8f6ca` |
| Overall entropy | 7.967 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 0 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 34,816 | 6.298 | No |
| `.data` | 512 | 0.857 | No |
| `.rdata` | 795,648 | 7.997 | ⚠️ Yes |
| `.pdata` | 2,048 | 3.928 | No |
| `.xdata` | 1,536 | 3.22 | No |
| `.bss` | 0 | 0.0 | No |
| `.idata` | 2,560 | 3.756 | No |
| `.tls` | 512 | -0.0 | No |
| `.rsrc` | 2,688 | 2.562 | No |
| `.reloc` | 512 | 2.064 | No |

### Imports

**bcrypt.dll**: `BCryptCloseAlgorithmProvider`, `BCryptDecrypt`, `BCryptDestroyKey`, `BCryptGenerateSymmetricKey`, `BCryptOpenAlgorithmProvider`, `BCryptSetProperty`
**KERNEL32.dll**: `DeleteCriticalSection`, `EnterCriticalSection`, `FreeLibrary`, `GetLastError`, `GetModuleHandleA`, `GetProcAddress`, `GetStartupInfoA`, `GetTickCount`, `InitializeCriticalSection`, `IsDBCSLeadByte`, `LeaveCriticalSection`, `LoadLibraryA`, `MultiByteToWideChar`, `SetUnhandledExceptionFilter`, `Sleep`
**msvcrt.dll**: `__C_specific_handler`, `__getmainargs`, `__initenv`, `__iob_func`, `__set_app_type`, `__setusermatherr`, `_acmdln`, `_amsg_exit`, `_cexit`, `_commode`, `_fmode`, `_initterm`, `abort`, `atexit`, `calloc`

## Extracted Strings

Total strings found: **1929** (showing first 100)

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
ASA[T\M
PSQY[XAVM
XVV^^H
[AWA_SH
AVUWVSH
D$0APAQAYAX
P[^_]A^
APAQAYAX
APAQAYAXARASA[AZAUM
PSQY[XP
APAQAYAXH
AYAPAX
ARASA[AZM
	QYAPAX
APAQAYAXH
AQAYARAZ
ARASA[AZM
ARASA[AZW
_APAQAYAXH
APAQAYAXM
ARASA[AZH
APAQAYAXM
ARASA[AZ
XQRZYL
?AWA_H
ARASA[AZH
APAQAYAXM
ARASA[AZL
TPQYXH
2_VV^^AVA^H
APAQAYAX
PXARASA[AZ
6~xaJ2
AYVW_^
ASA[RH
?VW_^H
ASA[RH
ARASA[AZM
CxAQAY
PSQY[X
AUA]f.
W_ASA[H
A	AQAY
A^PQYX
0OOOOH
i
ASA[AV
AUA]ARASA[AZ1
PQYXARAZ1
A\AQAYASA[1
PSQY[X
ARASA[AZ
APAQAYAXE1
T$hW_H
T$HAPAQAYAXM
VV^^SH
9MZu_M
AWAVAUATUWVSH
APAQAYAXM
h[^_]A\A]A^A_
PSQY[X
VV^^L;d$(
AWAVAUATUWVSH
?HcF<H
[^_]A\A]A^A_
AUA]QRZY
AVWVSH
X[^_A^
PSQY[XH
X[^_A^
AWAVAUATUWVSH
h[^_]A\A]A^A_
APAQAYAXM
ARASA[AZH
L$@ASA[L
AWA_AWA_
t|AUA]H
PHc5V{
UAWAVAUATWVSH
[^_A\A]A^A_]
([^_]H
@' t	H
wsnmp32.dll
objsel.dll
mfcore.dll
p2p.dll
hid.dll
wow64win.dll
mapi32.dll
msi.dll
d2d1.dll
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.1400082c0` | `0x1400082c0` | 32910 | ✓ |
| `fcn.1400095c0` | `0x1400095c0` | 32787 | ✓ |
| `fcn.140008ac0` | `0x140008ac0` | 2502 | ✓ |
| `fcn.1400079f0` | `0x1400079f0` | 1706 | ✓ |
| `fcn.140007280` | `0x140007280` | 1118 | ✓ |
| `fcn.140006790` | `0x140006790` | 1013 | ✓ |
| `fcn.140001010` | `0x140001010` | 976 | ✓ |
| `fcn.1400086f0` | `0x1400086f0` | 974 | ✓ |
| `fcn.140006f40` | `0x140006f40` | 819 | ✓ |
| `fcn.1400076e0` | `0x1400076e0` | 772 | ✓ |
| `fcn.1400064c0` | `0x1400064c0` | 707 | ✓ |
| `fcn.140003680` | `0x140003680` | 447 | ✓ |
| `fcn.140002e00` | `0x140002e00` | 441 | ✓ |
| `fcn.1400034c0` | `0x1400034c0` | 433 | ✓ |
| `fcn.140002fc0` | `0x140002fc0` | 430 | ✓ |
| `fcn.140003170` | `0x140003170` | 417 | ✓ |
| `fcn.140003320` | `0x140003320` | 411 | ✓ |
| `fcn.140008580` | `0x140008580` | 368 | ✓ |
| `fcn.140008e30` | `0x140008e30` | 258 | ✓ |
| `fcn.1400080a0` | `0x1400080a0` | 241 | ✓ |
| `fcn.140006dd0` | `0x140006dd0` | 201 | ✓ |
| `fcn.1400081a0` | `0x1400081a0` | 154 | ✓ |
| `fcn.140001b40` | `0x140001b40` | 150 | ✓ |
| `fcn.140001e90` | `0x140001e90` | 150 | ✓ |
| `fcn.140001f30` | `0x140001f30` | 137 | ✓ |
| `fcn.140001e00` | `0x140001e00` | 137 | ✓ |
| `fcn.140009070` | `0x140009070` | 128 | ✓ |
| `fcn.140002110` | `0x140002110` | 126 | ✓ |
| `fcn.140002410` | `0x140002410` | 126 | ✓ |
| `entry1` | `0x140008390` | 123 | ✓ |

### Decompiled Code Files

- [`code/entry1.c`](code/entry1.c)
- [`code/fcn.140001010.c`](code/fcn.140001010.c)
- [`code/fcn.140001b40.c`](code/fcn.140001b40.c)
- [`code/fcn.140001e00.c`](code/fcn.140001e00.c)
- [`code/fcn.140001e90.c`](code/fcn.140001e90.c)
- [`code/fcn.140001f30.c`](code/fcn.140001f30.c)
- [`code/fcn.140002110.c`](code/fcn.140002110.c)
- [`code/fcn.140002410.c`](code/fcn.140002410.c)
- [`code/fcn.140002e00.c`](code/fcn.140002e00.c)
- [`code/fcn.140002fc0.c`](code/fcn.140002fc0.c)
- [`code/fcn.140003170.c`](code/fcn.140003170.c)
- [`code/fcn.140003320.c`](code/fcn.140003320.c)
- [`code/fcn.1400034c0.c`](code/fcn.1400034c0.c)
- [`code/fcn.140003680.c`](code/fcn.140003680.c)
- [`code/fcn.1400064c0.c`](code/fcn.1400064c0.c)
- [`code/fcn.140006790.c`](code/fcn.140006790.c)
- [`code/fcn.140006dd0.c`](code/fcn.140006dd0.c)
- [`code/fcn.140006f40.c`](code/fcn.140006f40.c)
- [`code/fcn.140007280.c`](code/fcn.140007280.c)
- [`code/fcn.1400076e0.c`](code/fcn.1400076e0.c)
- [`code/fcn.1400079f0.c`](code/fcn.1400079f0.c)
- [`code/fcn.1400080a0.c`](code/fcn.1400080a0.c)
- [`code/fcn.1400081a0.c`](code/fcn.1400081a0.c)
- [`code/fcn.1400082c0.c`](code/fcn.1400082c0.c)
- [`code/fcn.140008580.c`](code/fcn.140008580.c)
- [`code/fcn.1400086f0.c`](code/fcn.1400086f0.c)
- [`code/fcn.140008ac0.c`](code/fcn.140008ac0.c)
- [`code/fcn.140008e30.c`](code/fcn.140008e30.c)
- [`code/fcn.140009070.c`](code/fcn.140009070.c)
- [`code/fcn.1400095c0.c`](code/fcn.1400095c0.c)

## Behavioral Analysis

### Analysis Summary
The provided code represents a sophisticated **packer or loader** typically used in malware to hide and decrypt the actual malicious payload. It utilizes multiple layers of decryption, dynamic API resolution, and memory manipulation to hide its true intent from static analysis.

---

### Core Functionality and Purpose
*   **Multi-Stage Payload Decryption:** The primary purpose of this code is to decrypt embedded resources (likely strings, configuration files, or secondary executable modules) before use. It uses custom obfuscation layers followed by standard Windows Cryptography APIs (`BCrypt` library).
*   **Dynamic API Resolution:** Rather than having a clear Import Address Table (IAT), the binary resolves many functions at runtime using `GetProcAddress`. This is done on strings that are only decrypted in memory, making it difficult for defenders to see what system capabilities the malware intends to use until it is actually running.
*   **Module Loading Engine:** The code contains logic to loop through and load various DLLs (some of which are non-standard or suspicious) to provide functionality such as networking or process manipulation.

---

### Suspicious or Malicious Behaviors
*   **Advanced Evasion via Encryption:** 
    *   The function `fcn.1400064c0` utilizes the **Windows BCrypt API** (`BCryptOpenAlgorithmProvider`, `BCryptGenerateSymmetricKey`, and `BCryptDecrypt`). This indicates that the program contains encrypted payloads that are decrypted in memory just before use.
*   **Runtime Unpacking & Memory Manipulation:** 
    *   The function `fcn.140008580` interacts with **`VirtualProtect`**. This is a classic sign of a packer or loader; it modifies the permissions of memory regions (e.g., making them "Executable") to allow a decrypted payload to run in the process's address space.
    *   It also appears to scan for "image-section" headers, suggesting it might be finding and executing code segments that aren't part of the original file on disk.
*   **Obfuscated String Decoding:** 
    *   Function `fcn.140006790` performs complex mathematical operations (XORing with `0x87`, bitwise rotations, and multiplication/addition loops) to "unpack" strings into a readable format. This is used to hide API names, IP addresses, or file paths from automated scanners.
*   **Suspicious DLL Loading:** 
    *   The inclusion of an extensive list of DLLs in the data section (e.g., `wsnmp32.dll`, `p2p.dll`, `hid.dll`) suggests the malware is seeking out various capabilities like network communication, hidden information gathering, or interacting with hardware.

---

### Notable Techniques and Patterns
*   **"Staged" Execution:** The code follows a classic "Loader" pattern:
    1.  Perform initial de-obfuscation of internal strings (via `fcn.140006790`).
    2.  Use those strings to resolve APIs via `GetProcAddress` (the `fcn.1400079f0` block).
    3.  Decrypt a primary payload using standard Windows crypto libraries (`BCrypt`).
    4.  Change memory permissions to execute the payload.
*   **Anti-Analysis Logic:** The heavy use of internal decryption functions and the absence of many plain-text strings in the code suggest a high level of effort to bypass static analysis (e.g., looking for suspicious imports or known malicious strings).
*   **Environment Check/Wait:** The presence of `GetTickCount` and calls to `Sleep` (in the `fcn.140001010` block) suggests a "wait-and-see" approach, potentially used to delay execution or bypass timing-based sandboxes.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of observed behaviors to MITRE ATT&CK techniques:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The use of XOR operations and complex mathematical loops (fcn.140006790) to decode strings hides API names, IPs, and file paths from static analysis. |
| **T1027.003** | Software Packing | The multi-stage decryption, the "loader" pattern, and the use of `VirtualProtect` to change memory permissions are classic indicators of a packer used to hide malicious code. |
| **T1497** | Virtualized Environment | The use of `GetTickCount` and `Sleep` functions (fcn.140001010) suggests the malware is attempting to stall execution or detect sandbox environments. |
| **T1036** | Modify Certificate Store (Implicit/Related Context) | While not a direct match for standard DLL loading, the specific inclusion of non-standard/suspicious DLLs in the data section suggests an intent to leverage specialized capabilities. |

***

**Analyst Notes:** 
*   The heavy reliance on **Dynamic API Resolution** (resolving functions via `GetProcAddress` from decrypted strings) is a primary mechanism used to support **T1027**, as it ensures that the Import Address Table (IAT) remains "clean" during initial static scans.
*   The sequence of **Decryption -> Memory Permission Change -> Execution** is the standard operational flow for a malicious loader/packer.

---

## Indicators of Compromise

Based on the strings and behavioral analysis provided, here are the extracted Indicators of Compromise (IOCs). 

Note: The "Extracted Strings" section consists primarily of high-entropy data and obfuscated junk code typical of a packer; therefore, no direct IP addresses or hashes were identified within that specific raw data block.

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   None identified. (While several DLLs like `wsnmp32.dll` and `p2p.dll` are mentioned, they appear as calls to system libraries rather than specific malicious file paths).

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified.

**Other artifacts (behavioral signatures & detection patterns)**
*   **Obfuscation Key:** XOR operation using the value `0x87` (used for de-obfuscating strings).
*   **Decryption Method:** Utilization of Windows **BCrypt library** (`BCryptOpenAlgorithmProvider`, `BCryptGenerateSymmetricKey`, `BCryptDecrypt`) to decrypt payloads in memory.
*   **Memory Manipulation:** Use of the `VirtualProtect` function to change memory permissions (e.g., making sections executable) to run decrypted code.
*   **Anti-Analysis Techniques:** Implementation of "wait" tactics using `GetTickCount` and `Sleep` to bypass automated sandbox analysis.
*   **Decoding Logic:** Complex mathematical operations involving bitwise rotations, multiplication, and addition loops to hide API names and configuration data.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Loader / Packer
3. **Confidence**: High (as a loader/packer; the final payload remains hidden)
4. **Key evidence**:
    *   **Staged Execution & Memory Manipulation:** The sample follows a classic loader lifecycle: decrypting strings via XOR loops, resolving APIs dynamically using `GetProcAddress`, and utilizing `VirtualProtect` to change memory permissions to execute decrypted payloads.
    *   **Sophisticated Obfuscation:** Use of the Windows `BCrypt` library for multi-stage decryption and complex mathematical operations (bit rotations/multiplication) to hide critical information like IP addresses and API names from static analysis.
    *   **Anti-Analysis Tactics:** The implementation of "wait" tactics (`GetTickCount` and `Sleep`) specifically designed to stall execution to bypass time-limited automated sandbox environments.
