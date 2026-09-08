# Threat Analysis Report

**Generated:** 2026-09-06 10:07 UTC
**Sample:** `14e2358e66c2dfd1aa283cc030a49110b06fd057cdebb9e96ff10e44ef0c012b_14e2358e66c2dfd1aa283cc030a49110b06fd057cdebb9e96ff10e44ef0c012b.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `14e2358e66c2dfd1aa283cc030a49110b06fd057cdebb9e96ff10e44ef0c012b_14e2358e66c2dfd1aa283cc030a49110b06fd057cdebb9e96ff10e44ef0c012b.exe` |
| File type | PE32+ executable for MS Windows 5.02 (GUI), x86-64 (stripped to external PDB), 9 sections |
| Size | 3,963,392 bytes |
| MD5 | `6b84cad087f5800df133658483a9ccaa` |
| SHA1 | `dc1f7527e5f39c5e1e1f19b2d574a6743cb1c6ae` |
| SHA256 | `14e2358e66c2dfd1aa283cc030a49110b06fd057cdebb9e96ff10e44ef0c012b` |
| Overall entropy | 7.999 |
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
| `.text` | 30,720 | 6.442 | No |
| `.data` | 1,024 | 5.486 | No |
| `.rdata` | 3,926,016 | 8.0 | ⚠️ Yes |
| `.pdata` | 1,024 | 2.536 | No |
| `.xdata` | 512 | 2.971 | No |
| `.bss` | 0 | 0.0 | No |
| `.idata` | 2,048 | 4.34 | No |
| `.tls` | 512 | -0.0 | No |
| `.reloc` | 512 | 1.541 | No |

### Imports

**ADVAPI32.dll**: `CryptAcquireContextA`, `CryptDecrypt`, `CryptDestroyKey`, `CryptImportKey`, `CryptReleaseContext`, `CryptSetKeyParam`
**KERNEL32.dll**: `CloseHandle`, `CreateToolhelp32Snapshot`, `DeleteCriticalSection`, `EnterCriticalSection`, `GetLastError`, `GetModuleHandleA`, `GetProcAddress`, `GetTickCount64`, `GlobalMemoryStatusEx`, `InitializeCriticalSection`, `LeaveCriticalSection`, `LoadLibraryA`, `Process32First`, `Process32Next`, `SetUnhandledExceptionFilter`
**msvcrt.dll**: `__C_specific_handler`, `__getmainargs`, `__initenv`, `__iob_func`, `__set_app_type`, `__setusermatherr`, `_amsg_exit`, `_cexit`, `_commode`, `_fmode`, `_initterm`, `abort`, `atexit`, `calloc`, `exit`

## Extracted Strings

Total strings found: **8821** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.data
.rdata
@.pdata
@.xdata
.idata
.reloc
AWAVAUATUWVSH
X[^_]A\A]A^A_
8MZuDHcP<H
xwLc%O
UAWAVAUATWVSH
[^_A\A]A^A_]
([^_]H
@' t	H
AWAVAUATVWUSH
D2\$QD
D2d$RD
D2D$SD2|$TD
D2t$VD
2T$W@2t$X
@2l$Z@
D$;2D$[2\$\
@2|$]@
D2T$^D
D2L$_D
D2l$cD
D2T$d@2t$eD
D2D$fD
D2d$gD
2L$h@2|$i
D2|$kD
D$;2D$l@2l$m
D2\$nD
D2t$oD
D2L$PD
D2l$RD
D2L$SD
D2d$TD
2D$UD2t$V
D2D$WD
@2|$X@
2T$Y@2t$Z
@2l$\@
D2|$]D2T$^D
D2\$_D
D$;2D$a
@2|$e@
D2\$fD2d$gD
D2L$hD
2D$jD2t$k
D2D$lD
D2|$mD
2L$n@2l$o
D$;2D$Q
D2T$RD
D2l$UD
D2|$VD
D2L$W@2|$XD
D2D$YD
D2t$ZD
2T$[@2t$\
@2l$^@
2L$_2\$`
D$;2D$a
D2\$bD
D2T$cD
@2t$eD
@2|$g@
D2\$h2D$iD
D2L$jD
D2d$kD
D$;2D$lD2t$m
D2|$oD
2T$PD2l$Q
D2D$RD
@2l$S@
D2T$TD
D2l$ZD
D2L$[D
D2d$\D
2D$]D2t$^
D2D$_D
@2|$`@
2T$a@2t$b
@2l$d@
D2|$eD2T$fD
D2\$gD
D$;2D$i
D2l$]D
D2|$^D
D2L$_@2|$`D
D2D$aD
D2t$bD
2T$c@2t$d
@2l$f@
2L$g2\$h
D$;2D$i
D2\$jD
D2T$kD
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.140002780` | `0x140002780` | 14640 | ✓ |
| `fcn.1400073b0` | `0x1400073b0` | 4897 | ✓ |
| `fcn.140001ce0` | `0x140001ce0` | 2486 | ✓ |
| `fcn.140006630` | `0x140006630` | 2207 | ✓ |
| `fcn.140006ed0` | `0x140006ed0` | 1233 | ✓ |
| `fcn.140001020` | `0x140001020` | 1024 | ✓ |
| `fcn.140001910` | `0x140001910` | 974 | ✓ |
| `fcn.1400060b0` | `0x1400060b0` | 882 | ✓ |
| `fcn.140006470` | `0x140006470` | 435 | ✓ |
| `fcn.1400017a0` | `0x1400017a0` | 368 | ✓ |
| `fcn.140002050` | `0x140002050` | 258 | ✓ |
| `fcn.1400014e0` | `0x1400014e0` | 242 | ✓ |
| `fcn.140002290` | `0x140002290` | 128 | ✓ |
| `entry1` | `0x1400015b0` | 123 | ✓ |
| `fcn.140001ec0` | `0x140001ec0` | 106 | ✓ |
| `fcn.140001740` | `0x140001740` | 96 | ✓ |
| `fcn.1400025a0` | `0x1400025a0` | 64 | ✓ |
| `fcn.140006430` | `0x140006430` | 60 | ✓ |
| `fcn.140002310` | `0x140002310` | 55 | ✓ |
| `fcn.1400023d0` | `0x1400023d0` | 54 | ✓ |
| `fcn.140002560` | `0x140002560` | 50 | ✓ |
| `fcn.140002650` | `0x140002650` | 31 | ✓ |
| `fcn.140001560` | `0x140001560` | 31 | ✓ |
| `entry0` | `0x140001420` | 29 | ✓ |
| `fcn.140002630` | `0x140002630` | 22 | ✓ |
| `entry2` | `0x140001590` | 21 | ✓ |
| `fcn.140002600` | `0x140002600` | 11 | ✓ |
| `fcn.140002620` | `0x140002620` | 11 | ✓ |
| `fcn.1400025e0` | `0x1400025e0` | 11 | ✓ |
| `fcn.1400025f0` | `0x1400025f0` | 11 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/entry1.c`](code/entry1.c)
- [`code/entry2.c`](code/entry2.c)
- [`code/fcn.140001020.c`](code/fcn.140001020.c)
- [`code/fcn.1400014e0.c`](code/fcn.1400014e0.c)
- [`code/fcn.140001560.c`](code/fcn.140001560.c)
- [`code/fcn.140001740.c`](code/fcn.140001740.c)
- [`code/fcn.1400017a0.c`](code/fcn.1400017a0.c)
- [`code/fcn.140001910.c`](code/fcn.140001910.c)
- [`code/fcn.140001ce0.c`](code/fcn.140001ce0.c)
- [`code/fcn.140001ec0.c`](code/fcn.140001ec0.c)
- [`code/fcn.140002050.c`](code/fcn.140002050.c)
- [`code/fcn.140002290.c`](code/fcn.140002290.c)
- [`code/fcn.140002310.c`](code/fcn.140002310.c)
- [`code/fcn.1400023d0.c`](code/fcn.1400023d0.c)
- [`code/fcn.140002560.c`](code/fcn.140002560.c)
- [`code/fcn.1400025a0.c`](code/fcn.1400025a0.c)
- [`code/fcn.1400025e0.c`](code/fcn.1400025e0.c)
- [`code/fcn.1400025f0.c`](code/fcn.1400025f0.c)
- [`code/fcn.140002600.c`](code/fcn.140002600.c)
- [`code/fcn.140002620.c`](code/fcn.140002620.c)
- [`code/fcn.140002630.c`](code/fcn.140002630.c)
- [`code/fcn.140002650.c`](code/fcn.140002650.c)
- [`code/fcn.140002780.c`](code/fcn.140002780.c)
- [`code/fcn.1400060b0.c`](code/fcn.1400060b0.c)
- [`code/fcn.140006430.c`](code/fcn.140006430.c)
- [`code/fcn.140006470.c`](code/fcn.140006470.c)
- [`code/fcn.140006630.c`](code/fcn.140006630.c)
- [`code/fcn.140006ed0.c`](code/fcn.140006ed0.c)
- [`code/fcn.1400073b0.c`](code/fcn.1400073b0.c)

## Behavioral Analysis

This updated analysis incorporates the new disassembly (chunk 2/2) into the existing profile. The addition of these functions provides significant technical depth into how the malware handles its internal data, masks its true intent, and navigates system resources to evade detection.

### **Updated Malware Analysis Report**

#### **Core Functionality and Purpose**
The binary remains confirmed as a **sophisticated packer/loader**. The new disassembly confirms that it employs a "layered" approach to information hiding:
1.  **Heavy Cryptography (via Windows APIs):** It doesn't just use simple XOR; it uses the `ADVAPI32` library (`CryptAcquireContextA`, `CryptImportKey`, `CryptDecrypt`) to handle high-level decryption of large data blocks. This is likely used for the primary payload or large configuration files.
2.  **Lightweight Obfuscation (Arithmetic/XOR loops):** For smaller, more frequent tasks—such as decoding internal commands, strings, or status flags—it uses a heavy mathematical "mangling" loop (`fcn.1400060b0`). This hides the logic from simple automated string scanners.
3.  **Dynamic API Resolution:** The malware avoids having a static Import Address Table (IAT) for sensitive functions. It resolves them at runtime using `GetProcAddress` and `GetModuleHandleA`, making it harder for security tools to flag it based on its "suspicious" imports alone.

---

#### **Newly Identified Technical Behaviors**
*   **Robust Decryption Pipeline (`fcn.140006470`):**
    *   This function is the workhorse of the decryption layer. It takes an encrypted blob, maps it to a temporary buffer, and uses `CryptImportKey` to inject a key into the system's crypto context before calling `CryptDecrypt`. 
    *   The fact that it uses **official Windows Crypto APIs** suggests that the malicious payloads are stored using industry-standard encryption (like AES or TripleDES), making them invisible to static analysis.

*   **Complex Arithmetic Obfuscation (`fcn.1400060b0`):**
    *   This function contains a massive, complex loop involving multiple shifts, XORs, and additions on data blocks of approximately 20KB (`0x3bda00`).
    *   This is designed to "dazzle" researchers. Even if the code is decrypted by one layer, this second layer ensures that internal configuration strings (like C2 URLs or stolen data paths) remain obscured until the very moment they are needed in memory.

*   **Dynamic API Hunting & Anti-Analysis (`fcn.140006ed0`):**
    *   This function systematically attempts to resolve and hook into system functions like `GetCurrentHwProfileA`.
    *   The presence of these checks, combined with the previous finding regarding **Timing Checks**, confirms a high level of environmental awareness. It is checking for specific hardware profiles to ensure it isn't running inside a virtual machine or a debugger-heavy sandbox environment.

*   **Multi-Stage Payload Staging (`fcn.140001020`):**
    *   The main execution flow includes several `strcmp` comparisons against the results of the decryption functions. 
    *   This confirms a **"Decision Tree" architecture**: The malware decodes a string, compares it to an internal constant (e.g., "Start_Injection" or "Check_Update"), and only then executes the next stage of the attack. This limits the amount of malicious behavior that occurs in any single function.

---

#### **Refined Indicators of Compromise (IoCs) & Tactics**
*   **Technique: API Obfuscation.** The use of `GetProcAddress` to resolve functions like `VirtualProtect` and others hidden in `fcn.140006ed0` means the malware will not exhibit its full capabilities until it is running in memory.
*   **Technique: Decryption via Crypto API.** By using `CryptImportKey`, the malware ensures that its main configuration is only "plain" in the system's RAM for a fraction of a second before use, making network captures or disk forensics less likely to find plain-text URLs.
*   **Technique: Loop-Based String Masking.** The heavy arithmetic loop (`fcn.1400060b0`) is specifically designed to defeat static analysis tools that look for high entropy or simple XOR patterns.

---

#### **Conclusion & Summary of Behavior**
The sample is a highly professionalized loader. It does not "just" run; it **negotiates with the environment**. 

1.  It checks if you are watching (Time and Hardware checks).
2.  It fetches its tools from a secret vault (CryptAcquireContext/Decrypt).
3.  It unscrambles its internal instructions using complex math (The heavy arithmetic loops).
4.  It only performs the "malicious" actions once it has confirmed all conditions are safe and data is ready.

**Recommendation:** Focus analysis on the memory space of `fcn.140006470` to capture the decrypted payloads in real-time, as they will likely appear only after this function successfully returns a non-null pointer.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027.002 | Obfuscated Files/Information: Packed String | The use of heavy cryptography (`CryptDecrypt`) and arithmetic "mangling" loops is designed to hide configuration data like C2 URLs from static analysis. |
| T1106 | Unified Evasion | The use of `GetProcAddress` and `GetModuleHandleA` to resolve functions at runtime avoids a static Import Address Table (IAT), hiding the malware's capabilities from automated scanners. |
| T1405 | Virtualization/Sandbox Detection | The implementation of timing checks and hardware profile lookups (`GetCurrentHwProfileA`) indicates the malware is checking for analysis environments before executing malicious payloads. |

---

## Indicators of Compromise

Based on the provided string data and behavioral analysis, here are the identified Indicators of Compromise (IOCs). 

Please note that the majority of the "Extracted Strings" section consists of obfuscated data/garbage characters resulting from the malware's packing layers; therefore, no direct IP addresses or plain-text URLs were found in those segments.

**IP addresses / URLs / Domains**
*   None identified. (The analysis notes these are currently encrypted and only reside in memory briefly).

**File paths / Registry keys**
*   None identified.

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified.

**Other artifacts**
*   **Anti-Analysis/Environment Detection:** The binary utilizes `GetCurrentHwProfileA` to detect virtual machines and sandboxes.
*   **Cryptographic Implementation:** Use of Windows APIs `CryptAc1u_ContextA`, `CryptImportKey`, and `CryptDecrypt` to hide primary payloads and configuration files.
*   **Signature/Logic Offsets (Internal):** 
    *   `fcn.1400060b0`: Complex arithmetic loop for string masking/obfuscation.
    *   `fcn.140006470`: Decryption pipeline for handling encrypted blobs.
    *   `fcn.140006ed0`: Dynamic API resolution and environment check logic.
*   **Decision Tree Logic:** The malware utilizes a "Decision Tree" architecture (identified in the analysis) to evaluate internal flags (e.g., checking conditions before proceeding with injection or updates).

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High

**Key evidence**:
*   **Multi-Layered Obfuscation:** The sample employs a sophisticated "layered" approach to hiding its intent, utilizing both official Windows Crypto APIs (`CryptDecrypt`) for primary payload decryption and complex arithmetic "mangling" loops to mask internal configuration strings.
*   **Advanced Evasion Techniques:** The malware actively checks for analysis environments through timing checks and hardware profile lookups (`GetCurrentHwProfileA`), combined with dynamic API resolution to hide its Import Address Table (IAT).
*   **Decoupled Execution Logic:** The use of a "Decision Tree" architecture confirms the sample is designed as a gatekeeper; it only executes malicious payloads after verifying that the environment is safe and all internal conditions are met, which is a hallmark of professionalized loaders.
