# Threat Analysis Report

**Generated:** 2026-08-23 21:10 UTC
**Sample:** `11b73673fda1fdb2d76dff99684800e3a3d81ce1ff3f84126225ff6652bea3bd_11b73673fda1fdb2d76dff99684800e3a3d81ce1ff3f84126225ff6652bea3bd.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `11b73673fda1fdb2d76dff99684800e3a3d81ce1ff3f84126225ff6652bea3bd_11b73673fda1fdb2d76dff99684800e3a3d81ce1ff3f84126225ff6652bea3bd.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, 5 sections |
| Size | 83,160 bytes |
| MD5 | `0941db839a7348a736297a571595603b` |
| SHA1 | `e7f434540ab04263f2c4318245e9b7345cae86b2` |
| SHA256 | `11b73673fda1fdb2d76dff99684800e3a3d81ce1ff3f84126225ff6652bea3bd` |
| Overall entropy | 6.517 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1730137267 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 40,448 | 6.581 | No |
| `.rdata` | 24,064 | 4.843 | No |
| `.data` | 2,048 | 2.012 | No |
| `.rsrc` | 512 | 4.704 | No |
| `.reloc` | 3,584 | 6.496 | No |

### Imports

**KERNEL32.dll**: `LocalFree`, `GetProcAddress`, `LoadLibraryA`, `Sleep`, `LocalAlloc`, `GetModuleFileNameW`, `DecodePointer`, `UnhandledExceptionFilter`, `SetUnhandledExceptionFilter`, `GetCurrentProcess`, `TerminateProcess`, `IsProcessorFeaturePresent`, `QueryPerformanceCounter`, `GetCurrentProcessId`, `GetCurrentThreadId`
**CRYPT32.dll**: `CertDeleteCertificateFromStore`, `CryptMsgGetParam`, `CertCloseStore`, `CryptQueryObject`, `CertAddCertificateContextToStore`, `CertFindAttribute`, `CertFreeCertificateContext`, `CertCreateCertificateContext`, `CertOpenSystemStoreA`

## Extracted Strings

Total strings found: **426** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
@.reloc
M;Jr

38_^]
E9xt
URPQQh
kUQPXY]Y[
< t1<	t-
uj Y;E
tf;1u
WWWPWS
u-PWWS
Pjh4
SSVWh 
f9:t!V
WuVVS
QQSWj0j@
xg;5x!A
x';x!A
u9Mu!3
PPPPPPPP
PPPPPWS
PP9E u:PPVWP
x$;x!A
t;Et
x7;5x!A

u,jXj

u	jZf
x7;5x!A
\9EuY
__based(
__cdecl
__pascal
__stdcall
__thiscall
__fastcall
__vectorcall
__clrcall
__eabi
__swift_1
__swift_2
__swift_3
__ptr64
__restrict
__unaligned
restrict(
 delete
operator
`vftable'
`vbtable'
`vcall'
`typeof'
`local static guard'
`string'
`vbase destructor'
`vector deleting destructor'
`default constructor closure'
`scalar deleting destructor'
`vector constructor iterator'
`vector destructor iterator'
`vector vbase constructor iterator'
`virtual displacement map'
`eh vector constructor iterator'
`eh vector destructor iterator'
`eh vector vbase constructor iterator'
`copy constructor closure'
`udt returning'
`local vftable'
`local vftable constructor closure'
 new[]
 delete[]
`omni callsig'
`placement delete closure'
`placement delete[] closure'
`managed vector constructor iterator'
`managed vector destructor iterator'
`eh vector copy constructor iterator'
`eh vector vbase copy constructor iterator'
`dynamic initializer for '
`dynamic atexit destructor for '
`vector copy constructor iterator'
`vector vbase copy constructor iterator'
`managed vector copy constructor iterator'
`local static thread guard'
operator "" 
operator co_await
operator<=>
 Type Descriptor'
 Base Class Descriptor at (
 Base Class Array'
 Class Hierarchy Descriptor'
 Complete Object Locator'
`anonymous namespace'
FlsAlloc
FlsFree
FlsGetValue
FlsSetValue
InitializeCriticalSectionEx
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00408d38` | `0x408d38` | 2957 | ✓ |
| `fcn.00402770` | `0x402770` | 1396 | ✓ |
| `fcn.00407570` | `0x407570` | 922 | ✓ |
| `fcn.00406e22` | `0x406e22` | 770 | ✓ |
| `fcn.0040917e` | `0x40917e` | 614 | ✓ |
| `main` | `0x401000` | 570 | ✓ |
| `fcn.0040a495` | `0x40a495` | 563 | ✓ |
| `fcn.00407ab4` | `0x407ab4` | 541 | ✓ |
| `fcn.004099d3` | `0x4099d3` | 536 | ✓ |
| `fcn.00408a92` | `0x408a92` | 524 | ✓ |
| `fcn.00403452` | `0x403452` | 523 | ✓ |
| `fcn.0040953e` | `0x40953e` | 523 | ✓ |
| `fcn.00406b6f` | `0x406b6f` | 520 | ✓ |
| `fcn.004052eb` | `0x4052eb` | 497 | ✓ |
| `fcn.0040a292` | `0x40a292` | 480 | ✓ |
| `fcn.00401bd4` | `0x401bd4` | 468 | ✓ |
| `fcn.00408417` | `0x408417` | 435 | ✓ |
| `fcn.00404f96` | `0x404f96` | 404 | ✓ |
| `fcn.004048bb` | `0x4048bb` | 400 | ✓ |
| `entry0` | `0x401489` | 390 | ✓ |
| `fcn.00404ae1` | `0x404ae1` | 388 | ✓ |
| `fcn.00403077` | `0x403077` | 373 | ✓ |
| `fcn.00402cf0` | `0x402cf0` | 371 | ✓ |
| `fcn.004020b0` | `0x4020b0` | 346 | ✓ |
| `fcn.00406507` | `0x406507` | 330 | ✓ |
| `fcn.00403b40` | `0x403b40` | 321 | ✓ |
| `fcn.00404573` | `0x404573` | 315 | ✓ |
| `fcn.0040887a` | `0x40887a` | 301 | ✓ |
| `fcn.00409f44` | `0x409f44` | 299 | ✓ |
| `fcn.00402f53` | `0x402f53` | 292 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.00401bd4.c`](code/fcn.00401bd4.c)
- [`code/fcn.004020b0.c`](code/fcn.004020b0.c)
- [`code/fcn.00402770.c`](code/fcn.00402770.c)
- [`code/fcn.00402cf0.c`](code/fcn.00402cf0.c)
- [`code/fcn.00402f53.c`](code/fcn.00402f53.c)
- [`code/fcn.00403077.c`](code/fcn.00403077.c)
- [`code/fcn.00403452.c`](code/fcn.00403452.c)
- [`code/fcn.00403b40.c`](code/fcn.00403b40.c)
- [`code/fcn.00404573.c`](code/fcn.00404573.c)
- [`code/fcn.004048bb.c`](code/fcn.004048bb.c)
- [`code/fcn.00404ae1.c`](code/fcn.00404ae1.c)
- [`code/fcn.00404f96.c`](code/fcn.00404f96.c)
- [`code/fcn.004052eb.c`](code/fcn.004052eb.c)
- [`code/fcn.00406507.c`](code/fcn.00406507.c)
- [`code/fcn.00406b6f.c`](code/fcn.00406b6f.c)
- [`code/fcn.00406e22.c`](code/fcn.00406e22.c)
- [`code/fcn.00407570.c`](code/fcn.00407570.c)
- [`code/fcn.00407ab4.c`](code/fcn.00407ab4.c)
- [`code/fcn.00408417.c`](code/fcn.00408417.c)
- [`code/fcn.0040887a.c`](code/fcn.0040887a.c)
- [`code/fcn.00408a92.c`](code/fcn.00408a92.c)
- [`code/fcn.00408d38.c`](code/fcn.00408d38.c)
- [`code/fcn.0040917e.c`](code/fcn.0040917e.c)
- [`code/fcn.0040953e.c`](code/fcn.0040953e.c)
- [`code/fcn.004099d3.c`](code/fcn.004099d3.c)
- [`code/fcn.00409f44.c`](code/fcn.00409f44.c)
- [`code/fcn.0040a292.c`](code/fcn.0040a292.c)
- [`code/fcn.0040a495.c`](code/fcn.0040a495.c)
- [`code/main.c`](code/main.c)

## Behavioral Analysis

### **Analysis Summary**

The binary functions as a **downloader or loader** designed to extract configuration data (such as a file path or command) from the system's certificate store and then execute that information using "Living off the Land" (LotL) techniques.

---

### **Core Functionality & Purpose**
The primary purpose of this code is to retrieve hidden information and launch an external payload. Instead of having a hardcoded URL or file path (which would be easily flagged by security scanners), it hides its configuration inside a certificate in the `TrustedPublisher` store. 

1.  **Data Retrieval:** It searches the `TrustedPublisher` certificate store for specific attributes, particularly looking for the Object Identifier (OID) `1.3.6.1.4.1.311.4.1.1`.
2.  **Persistence/Evasion of Config:** If it finds the expected data in the certificate, it parses this information to construct a command or path.
3.  **Delayed Execution:** The program calls `Sleep(40000)` (approx. 40 seconds) after loading the necessary components but before executing the final payload. This is intended to bypass sandbox analysis by waiting out common automated scan timers.
4.  **Execution via System Binaries:** It uses `LoadLibraryA("dfshim")` and `GetProcAddress` to obtain `ShOpenVerbApplicationW`. This allows it to execute a command using standard Windows shell execution logic, making the subsequent process appear more legitimate to security tools.

---

### **Suspicious & Malicious Behaviors**

*   **Certificate Store as a Configuration Database:**
    *   The use of `CertOpenSystemStoreA` (specifically "TrustedPublisher") and `CryptQueryObject` to fetch data is a highly suspicious technique used by advanced malware (e.g., certain backdoors and trojans) to hide configuration details like C2 servers or drop paths in an area rarely monitored by standard security products.
*   **Anti-Analysis / Sandbox Evasion:**
    *   The **40-second sleep timer** (`Sleep(40000)`) is a classic technique used to evade automated malware sandboxes, which often stop analysis after 30–60 seconds of execution.
*   **Living off the Land (LotL):**
    *   By invoking `dfshim` and `ShOpenVerbApplicationW`, the malware avoids calling `CreateProcess` or `ShellExecute` directly on a suspicious path. Instead, it passes its payload to an official Windows component that handles the execution, making the launch appear as a standard system-initiated action.
*   **Post-Execution Cleanup:**
    *   The loop at the end of `main` calling `CertDeleteCertificateFromStore` suggests an attempt to "clean up" and remove evidence of the configuration retrieval or any temporary certificate handles created during execution, likely to hide its footprint after the payload has been launched.

---

### **Notable Techniques & Patterns**

*   **OID-Based Filtering:** The specific check for `1.3.6.1.4.1.311.4.1.1` is a precise way of targeting specific fields within a certificate (often used to identify third-party software or specific vendor properties).
*   **Dynamic API Resolution:** The use of `GetProcAddress` for core system functions (like those in `dfshim`) indicates an effort to hide the imports from static analysis tools.
*   **Large Math Library Inclusion:** Functions like `fcn.0040917e` and `fcn.00409f44` show extensive floating-point logic. While these appear to be standard math functions (sine, square root), their presence in a small loader might suggest the binary was built with a large compiler stack or contains enough "junk" code/bloat to complicate analysis and size-up the file's complexity.
*   **Obfuscated String Handling:** The logic in `fcn.00403077` indicates complex handling of quoted paths and escape characters, typical when building command strings for execution from raw data extracted from a certificate.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The malware hides configuration data (C2 info/paths) inside certificate fields and OIDs to avoid detection by automated security scanners. |
| **T1106** | Native API | The use of `GetProcAddress` to resolve functions like those in `dfshim` at runtime is used to hide the Import Address Table (IAT) from static analysis. |
| **T1218** | System Binary Proxy Execution | The malware uses `dfshim` and `ShOpenVerbApplicationW` as a "Living off the Land" proxy to execute commands through legitimate Windows binaries. |
| **T1070** | Indicator Removal on Host | The final loop utilizing `CertDeleteCertificateFromStore` is a cleanup mechanism designed to remove traces of certificate-based configuration retrieval. |

---

## Indicators of Compromise

Based on the strings and behavioral analysis provided, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *(None found)*

**File paths / Registry keys**
*   **Certificate Store:** `TrustedPublisher` (Used as a non-standard configuration database for hidden values)
*   *Note: The string `C:\builds\cc\cwcontrol\Product\ClickOnceRunner\Release\ClickOnceRunner.pdb` was identified but excluded as it is a standard developer build path/PDB file and not an active malicious path.*

**Mutex names / Named pipes**
*   *(None found)*

**Hashes**
*   *(None found)*

**Other artifacts**
*   **OID (Object Identifier):** `1.3.6.1.4.1.311.4.1.1` (Specific identifier used to filter and extract configuration data from certificates)
*   **Execution Patterns:** 
    *   Use of `dfshim` (`dfshim.dll`) and `ShOpenVerbApplicationW` for Living off the Land (LotL) execution.
    *   Dynamic API resolution via `GetProcAddress`.
*   **Evasion Tactics:**
    *   **Sleep Timer:** `40000` (A 40-second sleep interval used to bypass automated sandbox analysis).
    *   **Evidence Cleanup:** Usage of `CertDeleteCertificateFromStore` to remove traces of the configuration certificate after execution.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://cacerts.digicert.com/DigiCertAssuredIDRootCA.crt0E`
- `http://cacerts.digicert.com/DigiCertTrustedG4CodeSigningRSA4096SHA3842021CA1.crt0`
- `http://cacerts.digicert.com/DigiCertTrustedG4RSA4096SHA256TimeStampingCA.crt0`
- `http://cacerts.digicert.com/DigiCertTrustedRootG4.crt0C`
- `http://crl3.digicert.com/DigiCertAssuredIDRootCA.crl0`
- `http://crl3.digicert.com/DigiCertTrustedG4CodeSigningRSA4096SHA3842021CA1.crl0S`
- `http://crl3.digicert.com/DigiCertTrustedG4RSA4096SHA256TimeStampingCA.crl0`
- `http://crl3.digicert.com/DigiCertTrustedRootG4.crl0`
- `http://crl4.digicert.com/DigiCertTrustedG4CodeSigningRSA4096SHA3842021CA1.crl0`
- `http://ocsp.digicert.com0`
- `http://ocsp.digicert.com0A`
- `http://ocsp.digicert.com0C`
- `http://ocsp.digicert.com0X`
- `http://www.digicert.com/CPS0`

---

## Malware Family Classification

Based on the analysis provided, here is the classification:

1. **Malware family:** Unknown
2. **Malware type:** Loader / Downloader
3. **Confidence:** High (regarding functionality and intent)
4. **Key evidence:**
    *   **Advanced Configuration Obfuscation:** The use of a specific Object Identifier (OID) within the `TrustedPublisher` certificate store to hide configuration data is a sophisticated evasion technique designed to bypass static analysis and signature-based detection.
    *   **Sophisticated Evasion Tactics:** The inclusion of a 40-second sleep timer specifically targets the time limits of automated sandboxes, combined with "Living off the Land" (LotL) techniques using `dfshim` and `ShOpenVerbApplicationW` to mask execution from security tools.
    *   **Anti-Forensics Cleanup:** The final step of deleting certificates used for configuration (`CertDeleteCertificateFromStore`) indicates a deliberate attempt to remove traces of the malware's activity on the host machine.
