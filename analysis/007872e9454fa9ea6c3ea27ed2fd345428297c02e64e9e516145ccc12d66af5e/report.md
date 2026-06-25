# Threat Analysis Report

**Generated:** 2026-06-24 15:40 UTC
**Sample:** `007872e9454fa9ea6c3ea27ed2fd345428297c02e64e9e516145ccc12d66af5e_007872e9454fa9ea6c3ea27ed2fd345428297c02e64e9e516145ccc12d66af5e.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `007872e9454fa9ea6c3ea27ed2fd345428297c02e64e9e516145ccc12d66af5e_007872e9454fa9ea6c3ea27ed2fd345428297c02e64e9e516145ccc12d66af5e.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, 5 sections |
| Size | 83,176 bytes |
| MD5 | `0abbfde3b1408ccca026d2b2ae8c6719` |
| SHA1 | `2fb78b71c38d49a190cdfba114e10e4851733104` |
| SHA256 | `007872e9454fa9ea6c3ea27ed2fd345428297c02e64e9e516145ccc12d66af5e` |
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

Based on my analysis of the provided disassembly, this binary exhibits behavior consistent with a **"Living off the Land" (LotL) downloader or a "dropper"** that uses digital certificate metadata as a carrier for additional information (likely a path to a second-stage payload).

### Core Functionality and Purpose
The primary purpose of this code is to inspect its own (or related) digital signature, extract specific data from the certificate's extended attributes, and then use a system utility (`dfshim.dll`) to execute a command or open a remote location.

### Suspicious/Malicious Behaviors
*   **Certificate Scraping for Hidden Data:** 
    The code uses `CertOpenSystemStoreA` (targeting "TrustedPublisher") and `CryptQueryObject`. It then iterates through the certificate's properties using `CryptMsgGetParam`. Specifically, it looks for a very specific OID: `"1.3.6.1.4.1.311.4.1.1"`. This is often used in multi-stage attacks where the "malicious" configuration (like a URL or file path) is hidden inside the certificate's metadata rather than in the binary's strings, making it harder for static analysis to detect.
*   **Use of `dfshim` and `ShOpenVerbApplicationW`:** 
    If the certificate check succeeds, the program loads `dfshim.dll` and resolves `ShOpenVerbApplicationW`. This is a classic **Living off the Land (LotL)** technique. Instead of calling a shell command directly (which triggers alerts), it leverages the Windows "Downloader File Shim" to handle the execution of a target application or URI.
*   **Anti-Analysis Sleep:** 
    The code explicitly calls `Sleep(40000)` (40 seconds) after attempting to trigger the secondary action via `dfshim`. This is a common anti-sandbox technique used to bypass automated analysis tools that only monitor the process for a few seconds.
*   **Trace Cleanup:** 
    After the sleep, it attempts to "clean up" by calling `CertDeleteCertificateFromStore` and closing certificates, attempting to leave as small of a footprint as possible in memory or system logs.

### Notable Techniques & Patterns
*   **Hidden Persistence/Execution Logic:** By using `ShOpenVerbApplicationW`, the malware offloads the actual execution logic to a trusted Windows component, potentially bypassing basic EDR rules that only monitor standard shell spawning (e.g., `cmd.exe` or `powershell.exe`).
*   **Certificate Parsing as an Information Channel:** The use of specific OIDs in `CRYPT32.dll` functions suggests the binary is designed to find a "hidden" command hidden within its own signed metadata.
*   **High Complexity/Obfuscated Logic:** Several internal functions (e.g., `fcn.00402770`, `fcn.00407570`) show complex loop structures and pointer arithmetic, common in software that is either heavily compiled from a large framework or intentionally obfuscated to hinder manual analysis of data transformation routines.

**Conclusion:** 
This binary likely acts as an **initial-stage loader**. It uses certificate attributes as a covert channel for instructions and leverages legitimate Windows system files (`dfshim`) to execute subsequent stages, while employing timing delays to evade automated sandboxes.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Information | The malware uses specific OIDs within certificate metadata as a covert channel to store configuration data, hiding it from standard static string analysis. |
| **T1218** | System Binary Proxy Execution | The binary utilizes the `dfshim.dll` (Downloader File Shim) and `ShOpenVerbApplicationW` to execute commands via trusted Windows components. |
| **T1497** | Virtualization/Sandbox Evasion | The inclusion of a 40-second sleep timer is designed to bypass automated sandbox analysis tools that only monitor process behavior for short durations. |
| **T1070** | Indicator Removal on Host | The execution of `CertDeleteCertificateFromStore` and closing of handles suggests an attempt to remove forensic artifacts and minimize the file's footprint. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs) categorized by type:

**IP addresses / URLs / Domains**
*   *(None identified)* — Note: The analysis suggests that payloads (URLs/Paths) are hidden within certificate metadata rather than being stored in plain text.

**File paths / Registry keys**
*   `dfshim.dll` (Note: Used as a "Living off the Land" component to execute remote locations or secondary payloads.)

**Mutex names / Named pipes**
*   *(None identified)*

**Hashes**
*   *(None identified)*

**Other artifacts**
*   **OID (Object Identifier):** `1.3.6.1.4.1.311.4.1.1` (Identified as the specific identifier used to locate hidden configuration data within a certificate's extended attributes.)
*   **Windows API Functions:** `ShOpenVerbApplicationW` (Associated with LotL execution of payloads via `dfshim.dll`).
*   **Anti-Analysis Technique:** `Sleep(40000)` (A 40-second sleep timer used to bypass automated sandbox analysis).
*   **Cryptographic Library Interaction:** `CRYPT32.dll` / `CertOpenSystemStoreA` (Used specifically for scraping the "TrustedPublisher" store).

---
**Analyst Note:**
The primary threat profile of this sample is a **loader/dropper**. It does not contain hardcoded C2 infrastructure in its strings; instead, it utilizes **Certificate Scraping** to retrieve hidden instructions. The use of `dfshim.dll` and the `1.3.6.1.4.1.311.4.1.1` OID are the primary technical indicators for identifying this specific threat actor's behavior.

---

## Malware Family Classification

1. **Malware family**: Custom
2. **Malware type**: loader
3. **Confidence**: High

**Key evidence**:
* **Certificate Scraping for Obfuscation:** The use of specific OIDs (e.g., `1.3.6.1.4.1.311.4.1.1`) to extract configuration data from certificate metadata is a sophisticated method to hide command-and-control (C2) information from static analysis.
* **Living off the Land (LotL) Execution:** The reliance on `dfshim.dll` and `ShOpenVerbApplicationW` indicates a deliberate attempt to bypass EDR/AV by using trusted system binaries to execute secondary payloads or remote URIs.
* **Sandbox Evasion:** The specific 40-second sleep timer is a classic signature used to exhaust the "timeout" window of automated analysis environments before malicious behavior begins.
