# Threat Analysis Report

**Generated:** 2026-08-24 23:06 UTC
**Sample:** `1213487c618b6db0b11b2eb89747740341602127456c4611c1feee1bd9d55ca0_1213487c618b6db0b11b2eb89747740341602127456c4611c1feee1bd9d55ca0.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `1213487c618b6db0b11b2eb89747740341602127456c4611c1feee1bd9d55ca0_1213487c618b6db0b11b2eb89747740341602127456c4611c1feee1bd9d55ca0.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, 5 sections |
| Size | 83,336 bytes |
| MD5 | `bf7deaa4aad3e5231a85da265976adc9` |
| SHA1 | `35226f115a5a1dba709a47163c4ef388dd83ddc9` |
| SHA256 | `1213487c618b6db0b11b2eb89747740341602127456c4611c1feee1bd9d55ca0` |
| Overall entropy | 6.513 |
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

Based on the analysis of the provided disassembly and decompiled code, here is a summary of the malware's behavior:

### Core Functionality and Purpose
The binary functions primarily as a **Certificate Installer** or **Trust-Manipulator**. Its main purpose is to programmatically inject certificates into the Windows system's trusted store and subsequently execute further components by leveraging system "shim" libraries. While much of the included code consists of standard math and library glue (e.g., floating-point logic, codepage handling), the `main` function contains the primary malicious logic.

### Suspicious or Malicious Behaviors
*   **Certificate Store Manipulation**: The program specifically targets the `TrustedPublisher` certificate store (`CertOpenSystemStoreA`). It iterates through a set of internal data (likely embedded in the binary) to:
    *   Generate new certificate contexts.
    *   Inject these certificates into the system's Trusted Publisher store.
    *   The use of the specific OID `1.3.6.1.4.1.311.4.1.1` confirms it is targeting **Microsoft Extended Key Usage for Code Signing**, intended to make subsequent malicious code appear "trusted" by the OS.
*   **Evasive Execution (Shim Exploitation)**: Instead of calling `system()` or `CreateProcess` directly, the malware uses a more stealthy approach:
    *   It dynamically loads **`dfshim.dll`**.
    *   It retrieves the address of **`ShOpenVerbApplicationW`**.
    *   This technique is often used to bypass security controls that monitor standard execution APIs by using "shims" (intended for backward compatibility) to launch payloads.
*   **Delayed Execution**: The `main` function contains a call to `Sleep(40000)` (approximately 40 seconds). This is a common anti-analysis technique used to "outwait" automated sandboxes or delay the execution of the payload until after initial telemetry collection has finished.

### Notable Techniques and Patterns
*   **Persistence through Trust**: By installing certificates into the `TrustedPublisher` store, the malware establishes a long-term foothold where subsequent malicious components can execute without triggering "Unknown Publisher" warnings.
*   **Abuse of System DLLs**: The reliance on `CryptMsgGetParam` to unpack configuration data and `dfshim.dll` for execution indicates an attempt to blend in with legitimate Windows management behavior.
*   **Standard Library Bloat/Wrapping**: A large portion of the code (e.g., `fcn.0040917e`, `fcn.00406e22`) is boilerplate from a math library (calculating square roots, sines, and cosines). This can sometimes be used as "padding" to increase the size of the file or hide malicious logic among thousands of lines of benign code.

### Summary Table
| Feature | Observation | Risk Level |
| :--- | :--- | :--- |
| **Certificate Manipulation** | Injecting certificates into `TrustedPublisher` store | **High** |
| **Evasive Execution** | Utilizing `dfshim.dll` and `ShOpenVerbApplicationW` | **High** |
| **Anti-Analysis** | Long sleep timer (40s) before final execution | **Medium** |
| **Persistence** | Modifying system trust stores to bypass security alerts | **High** |

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the observed behaviors from the provided analysis to the relevant MITRE ATT&CK techniques and sub-techniques below:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1036** | Masquerading | The manipulation of the `TrustedPublisher` store is intended to mask the malware's identity, making malicious code appear as "trusted" to bypass security warnings. |
| **Defense Evasion** | (No specific sub-technique) | The use of `dfshim.dll` and `ShOpenVerbApplicationW` is a specific method used to bypass security controls that monitor standard execution APIs like `CreateProcess`. |
| **T1497** | Virtualization/Sandbox Detection | The inclusion of a long `Sleep(40000)` command is a common technique used to "outwait" automated sandbox analysis environments. |

***

### Analyst Notes:
*   **Certificate Manipulation:** While often categorized generally under **Defense Evasion**, the specific act of altering certificates to provide a false sense of legitimacy is best represented by **T1036 (Masquerading)**, as it targets the user's and the OS's trust perception.
*   **Shim Exploitation:** Because `dfshim.dll` is a legitimate Windows system component used for application compatibility, abusing it to hide execution from EDR/AV systems is a classic **Defense Evasion** tactic. Since there is no specific sub-technique in the current MITRE framework specifically for "shims," the primary category is used to denote the intent to bypass security monitoring.
*   **Delayed Execution:** The 40-second sleep timer is specifically designed to exceed the typical timeout period of automated sandboxes, ensuring that the malicious payload only triggers after the analysis environment has concluded its initial telemetry gathering.

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *None identified.*

**File paths / Registry keys**
*   **Path:** `C:\builds\cc\cwcontrol\Product\ClickOnceRunner\Release\ClickOnceRunner.pdb` (Note: This is a PDB path; while likely a compilation artifact, it serves as an identifier for the build environment).
*   **Certificate Store:** `TrustedPublisher` (Targeted for certificate injection to bypass security warnings).

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   *None identified.*

**Other artifacts**
*   **OID:** `1.3.6.1.4.1.311.4.1.1` (Specific OID for Microsoft Extended Key Usage for Code Signing; used to manipulate trust).
*   **Malicious DLL Loading:** `dfshim.dll` (Used for evasive execution).
*   **Evasive API Call:** `ShOpenVerbApplicationW` (Used via the shim library to bypass standard execution monitoring).
*   **Anti-Analysis Technique:** A sleep timer of **40 seconds** (`Sleep(40000)`) used to bypass automated sandbox analysis.
*   **Encryption/Decoding Library usage:** `CryptMsgGetParam` (Used to extract configuration data).

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

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High

4. **Key evidence**:
*   **Certificate Manipulation for Trust:** The malware specifically targets the `TrustedPublisher` store and uses a specific OID to inject certificates, ensuring that subsequent malicious payloads will not trigger "Unknown Publisher" warnings from Windows.
*   **Evasive Execution (Shim Exploitation):** By utilizing `dfshim.dll` and `ShOpenVerbApplicationW` instead of standard execution APIs like `CreateProcess`, the malware intentionally attempts to bypass EDR/AV monitoring systems.
*   **Anti-Analysis Techniques:** The inclusion of a 40-second `Sleep` timer is a documented technique used to "outwait" automated sandboxes, while the use of high-entropy mathematical libraries as padding suggests an attempt to obfuscate malicious logic within a large binary.
