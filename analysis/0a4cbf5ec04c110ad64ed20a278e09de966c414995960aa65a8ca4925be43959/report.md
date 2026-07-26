# Threat Analysis Report

**Generated:** 2026-07-24 21:02 UTC
**Sample:** `0a4cbf5ec04c110ad64ed20a278e09de966c414995960aa65a8ca4925be43959_0a4cbf5ec04c110ad64ed20a278e09de966c414995960aa65a8ca4925be43959.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0a4cbf5ec04c110ad64ed20a278e09de966c414995960aa65a8ca4925be43959_0a4cbf5ec04c110ad64ed20a278e09de966c414995960aa65a8ca4925be43959.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, 5 sections |
| Size | 83,176 bytes |
| MD5 | `910f594f9f2510f8b7ab1fea5000a3b4` |
| SHA1 | `44e844f16315e47da4023c56e67343a83bebc354` |
| SHA256 | `0a4cbf5ec04c110ad64ed20a278e09de966c414995960aa65a8ca4925be43959` |
| Overall entropy | 6.516 |
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

Based on the provided disassembly and decompiled code, here is a technical analysis of the binary's behavior.

### Core Functionality and Purpose
The primary purpose of this malware is **Certificate Injection** and **Trust Escalation**. Instead of performing direct malicious actions (like stealing files or encrypting data) in its initial stage, it modifies the local system's certificate store to establish a "trusted" status for specific entities. By inserting certificates into the `TrustedPublisher` store, the malware ensures that subsequent executions by itself or associated components will not trigger Windows security warnings or UAC prompts regarding untrusted software.

### Suspicious and Malicious Behaviors
The analysis reveals several significant red flags typical of advanced persistent threats (APTs) or high-end trojans:

*   **Certificate Store Manipulation:** 
    *   The `main` function specifically targets the `"TrustedPublisher"` store via `CertOpenSystemStoreA`.
    *   It iterates through certificate parameters (`CryptMsgGetParam`) and uses `CertAddCertificateContextToStore` to inject a certificate into that store. This is a classic technique used to bypass Windows "Unknown Publisher" warnings in the future.
*   **Living off the Land (LotL) Techniques:** 
    *   The code interacts with **`dfshim.dll`** and calls `ShOpenVerbApplicationW`. These are legitimate system components, but they are frequently abused by malware to execute payloads or bypass security controls because the actions originate from a trusted Windows DLL.
*   **Anti-Analysis/Sandbox Evasion:** 
    *   The code includes a **`Sleep(40000)`** (approximately 40 seconds) before performing cleanup operations (`CertDeleteCertificateFromStore`). This is a common "stalling" technique designed to exhaust the time limits of automated malware sandboxes, which often only monitor a sample for 30–60 seconds.
*   **Self-Cleaning Behavior:** 
    *   After the sleep period, the code calls `CertDeleteCertificateFromStore`. This suggests it is attempting to remove the "tracks" of its certificate injection, potentially cleaning up after injecting a secondary payload or simply trying to appear benign if forensics are performed after execution.

### Notable Techniques and Patterns
*   **Targeted OID Selection:** The code specifically checks for OIDs (Object Identifiers), such as `1.3.6.1.4.1.311.4.1.1`, which is often associated with Microsoft's standard certificate extensions. It uses these to validate the structure of the certificate it is processing before proceeding to the execution phase.
*   **Sophisticated API Usage:** The use of `CryptQueryObject` and multiple `CryptMsgGetParam` calls suggests a high level of complexity in how it handles certificates, likely parsing specific fields like the Public Key or Subject Name to verify "authenticity" before establishing trust.
*   **Use of System Shell Functions:** By calling `ShOpenVerbApplicationW`, the malware attempts to use standard system shell behavior to launch an application associated with a file extension or certificate property, making it harder for heuristic engines to flag the execution as suspicious compared to a direct `CreateProcess` call.

### Summary Table of Indicators
| Behavior Category | Observed Action | Purpose |
| :--- | :--- | :--- |
| **Trust Escalation** | Injection into `TrustedPublisher` store | Bypass security warnings for future persistence. |
| **Evasion** | `Sleep(40000)` call | Bypass time-limited automated sandbox analysis. |
| **Execution** | Loading `dfshim.dll` & `ShOpenVerbApplicationW` | "Living off the land" to execute payloads via trusted system tools. |
| **Anti-Forensics** | Call to `CertDeleteCertificateFromStore` | Remove evidence of trust manipulation after installation. |

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the observed behaviors from the provided technical analysis to the corresponding MITRE ATT&CK techniques and sub-techniques.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1497** | Virtualization/Sandbox Evasion | The `Sleep(40000)` call is a classic "stalling" technique used to exceed the time limits of automated malware analysis environments. |
| **T1059** | Command and Scripting Interpreter | The use of `ShOpenVerbApplicationW` leverages standard system shell functions to execute commands, helping the binary blend in with legitimate activity. |
| **T1070** | Indicator Removal | The call to `CertDeleteCertificateFromStore` is used to remove the certificate's presence from the local store to hide tracks after the operation is complete. |
| **T1564** | Dynamic Resolution | While primarily for resolution, this technique is often associated with high-level logic used to resolve trust paths or bypass specific integrity checks before execution. |

***Note on "Trust Escalation":*** *While MITRE ATT&K does not have a single dedicated ID specifically for "Certificate Store Manipulation," the behavior is classified under **Defense Evasion** because it manipulates system settings (the `TrustedPublisher` store) to bypass security warnings and ensure the longevity of malicious activity.*

---

## Indicators of Compromise

### INDICATORS OF COMPROMISE

**IP addresses / URLs / Domains**
*   *None identified.*

**File paths / Registry keys**
*   `C:\builds\cc\cwcontrol\Product\ClickOnceRunner\Release\ClickOnceRunner.pdb` (Note: This is a build-environment artifact, but unique to the binary's compilation history.)

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   *None identified.*

**Other artifacts**
*   **Certificate Store Target:** `TrustedPublisher` (The specific store manipulated for certificate injection).
*   **Object Identifier (OID):** `1.3.6.1.4.1.311.4.1.1` (Used to validate certificate structures).
*   **Living-off-the-Land (LotL) Component:** `dfshim.dll` (Utilized in conjunction with `ShOpenVerbApplicationW` for payload execution).
*   **Anti-Analysis Behavior:** `Sleep(40000)` (A 40-second stall used to bypass automated sandbox analysis).

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

Based on the analysis provided, here is the classification of the sample:

1. **Malware family**: Unknown
2. **Malware type**: Loader / Dropper
3. **Confidence**: High
4. **Key evidence**:
    *   **Trust Escalation & Persistence:** The primary function of the binary is manipulating the `TrustedPublisher` store via `CertAddCertificateContextToStore`. This identifies it as a component designed to prepare the environment for subsequent payloads by ensuring they execute without "Unknown Publisher" warnings or security alerts.
    *   **Evasive Execution (LotL):** The use of `dfshim.dll` and `ShOpenVerbApplicationW` indicates an intent to bypass local security controls by leveraging trusted system binaries to launch secondary components, a hallmark of sophisticated loaders.
    *   **Anti-Analysis Techniques:** The presence of a specific 40-second sleep timer (`Sleep(40000)`) before performing cleanup is a classic "stalling" tactic used specifically to bypass the time constraints of automated sandbox analysis environments.
